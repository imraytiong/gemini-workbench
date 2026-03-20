const imap = require('imap-simple');
const { simpleParser } = require('mailparser');
const TurndownService = require('turndown');
const fs = require('fs');
const path = require('path');

const turndownService = new TurndownService();

// Config
const GMAIL_USER = process.env.GMAIL_USER;
const GMAIL_PASS = process.env.GMAIL_PASS;
const TARGET_ALIAS = 'raymond.tiong+plaud@gmail.com';
const PROJECT_ROOT = '/home/raytiong/projects/rayintheloop_web';
const OUTPUT_DIR = path.join(PROJECT_ROOT, 'journal/voice_notes');
const PROCESSED_FILE = path.join(__dirname, '../processed_ids.json');

if (!GMAIL_USER || !GMAIL_PASS) {
    console.error('Error: GMAIL_USER and GMAIL_PASS environment variables must be set.');
    process.exit(1);
}

const config = {
    imap: {
        user: GMAIL_USER,
        password: GMAIL_PASS,
        host: 'imap.gmail.com',
        port: 993,
        tls: true,
        tlsOptions: { rejectUnauthorized: false },
        authTimeout: 3000
    }
};

/**
 * Load processed Message-IDs from a local file to avoid duplicates.
 */
function loadProcessedIds() {
    if (fs.existsSync(PROCESSED_FILE)) {
        try {
            return JSON.parse(fs.readFileSync(PROCESSED_FILE, 'utf8'));
        } catch (e) {
            return [];
        }
    }
    return [];
}

/**
 * Save processed Message-IDs to a local file.
 */
function saveProcessedIds(ids) {
    fs.writeFileSync(PROCESSED_FILE, JSON.stringify(ids, null, 2));
}

/**
 * Sanitize a string for use as a filename.
 */
function sanitizeFilename(str) {
    return str.replace(/[^a-z0-9]/gi, '_').toLowerCase().slice(0, 50).replace(/^_+|_+$/g, '');
}

/**
 * Strips CSS and style blocks from the content.
 */
function cleanContent(content) {
    // Remove <style> tags and their content
    content = content.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '');
    // Remove common inline CSS/Style blocks if they leaked as text
    content = content.replace(/blockquote\s*{[\s\S]*?}\s*\.list-item[\s\S]*?li\s*{[\s\S]*?}/gi, '');
    return content.trim();
}

/**
 * Extracts a descriptive title from the content.
 */
function extractTitle(content, fallbackSubject) {
    const lines = content.split('\n').map(l => l.trim()).filter(l => l.length > 0);
    
    // 1. Look for explicit Title line
    const explicitTitle = lines.find(l => /^Title:\s*/i.test(l));
    if (explicitTitle) return explicitTitle.replace(/^Title:\s*/i, '').trim();

    // 2. Look for first Heading (that isn't a Generic PLAUD heading like Core Synopsis)
    const genericHeadings = ['core synopsis', 'next move', 'summary', 'overview', 'the transcript is brief, no summary is needed. the original audio transcription is as follows:'];
    const firstHeading = lines.find(l => {
        if (/^#+\s+/.test(l)) {
            const h = l.replace(/^#+\s+/, '').toLowerCase();
            return !genericHeadings.includes(h);
        }
        return false;
    });
    if (firstHeading) return firstHeading.replace(/^#+\s+/, '').trim();

    // 3. Look for underlined heading (Markdown style)
    const underlinedIdx = lines.findIndex(l => /^-+$/ .test(l) || /^=+$/ .test(l));
    if (underlinedIdx > 0) {
        const h = lines[underlinedIdx - 1].toLowerCase();
        if (!genericHeadings.includes(h)) return lines[underlinedIdx - 1];
    }

    // 4. Look for the actual transcription content (Speaker blocks or quotes)
    const transcriptionIdx = lines.findIndex(l => l.toLowerCase().includes('original audio transcription is as follows') || l.startsWith('> Speaker'));
    if (transcriptionIdx !== -1 && lines.length > transcriptionIdx + 1) {
        let snippet = lines[transcriptionIdx + 1].replace(/^>\s*/, '').trim();
        // If it's a Speaker line, skip to the actual text
        if (/^Speaker\s+\d+/.test(snippet) && lines.length > transcriptionIdx + 2) {
            snippet = lines[transcriptionIdx + 2].replace(/^>\s*/, '').trim();
        }
        if (snippet.length > 0) {
            return snippet.slice(0, 60).trim() + (snippet.length > 60 ? '...' : '');
        }
    }

    // 5. Fallback: If "Core Synopsis" exists, take the first 60 chars of the next non-empty block
    const synopsisIdx = lines.findIndex(l => l.toLowerCase().includes('core synopsis'));
    if (synopsisIdx !== -1 && lines.length > synopsisIdx + 1) {
        let snippet = lines[synopsisIdx + 1];
        if (/^[-=]+$/.test(snippet) && lines.length > synopsisIdx + 2) {
            snippet = lines[synopsisIdx + 2];
        }
        return snippet.slice(0, 60).trim() + (snippet.length > 60 ? '...' : '');
    }

    // 6. Final fallback to first non-empty line
    if (lines.length > 0 && lines[0].length < 60) return lines[0];

    return fallbackSubject || 'Untitled Note';
}

/**
 * Determines a category based on keywords.
 */
function getCategory(content, subject) {
    const text = (content + ' ' + subject).toLowerCase();
    if (text.includes('meeting') || text.includes('sync') || text.includes('call')) return 'MEET';
    if (text.includes('task') || text.includes('todo') || text.includes('action item')) return 'TASK';
    if (text.includes('strategy') || text.includes('plan') || text.includes('exit')) return 'PLAN';
    if (text.includes('idea') || text.includes('brainstorm')) return 'IDEA';
    return 'NOTE';
}

async function gatherNotes() {
    let connection;
    try {
        if (!fs.existsSync(OUTPUT_DIR)) {
            fs.mkdirSync(OUTPUT_DIR, { recursive: true });
        }

        const processedIds = loadProcessedIds();
        connection = await imap.connect(config);
        await connection.openBox('INBOX');

        // Search for emails sent TO the specific alias
        const searchCriteria = [['TO', TARGET_ALIAS]];
        const fetchOptions = { bodies: ['HEADER', 'TEXT'], struct: true };

        const messages = await connection.search(searchCriteria, fetchOptions);
        console.log(`Found ${messages.length} messages matching criteria.`);

        const newProcessedIds = [...processedIds];
        let gatheredCount = 0;

        for (const message of messages) {
            const header = message.parts.find(part => part.which === 'HEADER');
            const messageId = header.body['message-id'][0];

            if (processedIds.includes(messageId)) {
                continue;
            }

            const all = message.parts.find(part => part.which === 'TEXT');
            const parsed = await simpleParser(all.body);

            const date = parsed.date || new Date();
            const dateStr = date.toISOString().split('T')[0];
            const timeStr = date.toTimeString().split(' ')[0].replace(/:/g, '');
            
            // Prioritize summary.txt attachment
            let content = '';
            const summaryAttachment = parsed.attachments.find(a => a.fileName === 'summary.txt');
            if (summaryAttachment) {
                content = summaryAttachment.content.toString('utf8');
            } else {
                // Fallback to email body
                content = parsed.text || '';
                if (parsed.html && (!parsed.text || parsed.text.trim().length < 10)) {
                    content = turndownService.turndown(parsed.html);
                }
            }

            // Clean up CSS/Style noise
            content = cleanContent(content);

            const subject = parsed.subject || 'Untitled Note';
            const descriptiveTitle = extractTitle(content, subject);
            const category = getCategory(content, subject);
            
            const titleSnippet = sanitizeFilename(descriptiveTitle);
            let filename = `${dateStr}_${category}_${titleSnippet}.md`;
            let filepath = path.join(OUTPUT_DIR, filename);

            // Ensure filename is truly unique in the output directory
            let counter = 1;
            while (fs.existsSync(filepath)) {
                filename = `${dateStr}_${category}_${titleSnippet}_${counter}.md`;
                filepath = path.join(OUTPUT_DIR, filename);
                counter++;
            }

            const markdown = `---
title: "${descriptiveTitle}"
date: ${date.toISOString()}
source: "PLAUD.AI"
original_subject: "${subject}"
category: "${category}"
tags: ["voice-note", "plaud", "${category.toLowerCase()}"]
---

${content}
`;

            fs.writeFileSync(filepath, markdown);
            console.log(`Saved: ${filename}`);
            newProcessedIds.push(messageId);
            gatheredCount++;
        }

        saveProcessedIds(newProcessedIds);
        console.log(`Finished: Gathered ${gatheredCount} new voice notes.`);

    } catch (err) {
        console.error('Error gathering notes:', err);
    } finally {
        if (connection) {
            connection.end();
        }
    }
}

gatherNotes();
