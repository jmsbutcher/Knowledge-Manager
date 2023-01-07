# Simple Knowledge Manager

### A desktop application for quick recording and retrieving of ideas by managing simple text files
Version 1.0 
January 7, 2023 
by James Butcher 
jmsbutcher1576@gmail.com 

<img src="https://github.com/jmsbutcher/Knowledge-Manager/blob/main/Images/GUIscreenshot1.PNG" class="img-fluid" alt="GUIscreenshot1">

## Purpose:

1. To serve as a useful tool for myself.
2. To improve my Python skills.
3. To improve my object-oriented design and architecture skills.
4. To learn unit testing and TDD.

## The idea:
<p>
  Often, while at work or working on something at home, I want to write down a useful tip or a link to a website that solves a problem I have that I may want to refer to again some day. I like to use simple text files for this because they are super fast to open, edit, and save. The problem is that these files start to pile up, or get lost across different folders. I also had no easy way of searching for the file I want. The Windows file explorer is just too slow and hard to use. 
  I envisioned this tool to serve as a hub for creating, modifying, and retrieving these text files. You can create one with a click of a button, add your content, perhaps add a keyword or two, and then save it. You can then find it again by searching for part of its title, or by filtering all files by topic or keyword.
</p>

## Usage:
1. Clone repository
2. Install prerequisites (To do: create prerequisites list)
3. Go to KnowledgeManager folder
4. Run "python3 main_window.py"

## Capabilities:
- Create document
- View document
- Edit document
- Delete document
- Search for document
- Filter documents by topic
- Filter documents by keyword
*All capabilities are for text files only

## Current state of project:
A mess. Incomplete, but working. I wanted to integrate it with Google could somehow, so it can sync the text documents across devices via Google Drive, but I was not able to get it to work in time. I may pick this back up again in the future.

A much more long-term goal would be to get this to work across desktop, mobile, and even ReMarkable 2 devices, so all my ideas can be synced up. It would also support different file formats and include images, pdfs, Ebooks, etc. Another cool idea would be to have documents link to each other like a graph, and then do all kinds of cool linking and analysis between ideas.
