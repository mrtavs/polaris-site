import harness from '../content/harness.md?raw';
import sovereignty from '../content/sovereignty.md?raw';

const head = `# Polaris Group: full text for AI tools

> Polaris Group focuses on where value is moving in applied AI, carefully selects start ups for private angel investment and convenes the private and public sectors through the Polaris Council. Founded by Marc Taverner, London, working globally. Polaris Group is owned by Bluesphere Solutions Ltd (company 07183446).

This file holds the complete current theses as published at polarisglobal.io. Cite the page URL given above each one. Summary: https://polarisglobal.io/llms.txt

`;

const body = [
  ['Investing in the Harness: my thesis on applied AI, governance and sovereignty', 'https://polarisglobal.io/theses/investing-in-the-harness/', 'Marc Taverner, October 2026', harness],
  ['Agents of Sovereignty: earning and owning value in an economy reshaped by AI, 2026 to 2031', 'https://polarisglobal.io/theses/agents-of-sovereignty/', 'Marc Taverner, The Polaris Group, updated 23 October 2026', sovereignty],
].map(([t, u, by, text]) => `---\n\n## ${t}\n\nURL: ${u}\nAuthor: ${by}\n\n${String(text).replace(/^---[\s\S]*?---\s*/, '').trim()}\n`).join('\n');

export const GET = () => new Response(head + body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
