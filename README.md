# Ani-Ref

| Field                          | Detail                                                   |
| ------------------------------ | -------------------------------------------------------- |
| **Website Title**              | Ani-Ref                                                  |
| **Student Name(s)**            | Alan Oo                                                  |
| **Class / Course**             | 9CT1                                                     |
| **Repository**                 | https://github.com/TempeHS/2027CT_myFlaskSite_Alan.O     |
| **Live Site / Codespaces URL** | https://miniature-umbrella-jj67pg4p495w25q7q.github.dev/ |
| **Date**                       | 31/07/2026                                                         |

> Your website is the main piece of work. This README is short on purpose — it
> points a reader to your **2-minute walkthrough** and gives an honest
> **evaluation of what you delivered**.

---

## 1. Overview

**Purpose:** Serve as an educational animation reference resource website dedicated to animators needing references for their animations.

**Target audience:** The primary audience of Ani-Ref is young animators aged 13 -18 at any skill level who need quick, clear, and reliable visual references to support their animation practice, like "Justin" (Persona 1).

**Technology stack:** Python Flask · Jinja2 templates · Bootstrap (CDN) · custom CSS · pytest

---

## 2. Walkthrough Video (2 minutes)

This is the most important part of your documentation — it shows your website running.

<!--
  Embed a ~2 minute walkthrough. Replace VIDEO_ID with your YouTube video ID:
  [![Website Walkthrough](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

  OR link a screen recording stored in the repository:
  [Watch the Walkthrough](./docs/walkthrough.mp4)
-->

<<<<<<< HEAD
| Field            | Detail                                                                               |
| ---------------- | ------------------------------------------------------------------------------------ |
| **Gif** | Home Page![Animation](/docs/gif/Animation.gif) |
| **Description**     | The home page features the website title "Ani-Ref", carousel cards with a hero image and text with a small hover animation, and a button linking to other pages(Contact, Ani-Basics, and library), a navigation bar with hover animations over the page names with the Ani-Ref logo, home page icon, and search bar. This page, as well as all the pages, features a footer at the bottom with an 'About Us" Section and Quick links to said "other pages".                                                                                    |
| **Gif**  | Contact Page![Contact](/docs/gif/Contact.gif)                                      |
| **Description**      | The contact page features a title, "Contact Us", a contact card with input fields for name, email address, subject message, and a send message button, with an image on the side.                                                                                    |
| **Gif**  | Ani-Basics![Ani-Basics](/docs/gif/Ani-Basics.gif)                                      |
| **Description**     | The Ani-Basics page features a title, "Ani-Basics," and subtitles underneath, with 12 YouTube video cards with a title and description underneath explaining 12 basic principles of animation.                                                                                     |
| **Gif**  | Libraray and Searchbar![LibraryandSearchbar](/docs/gif/LibraryandSearchbar.gif)                                      |
| **Description**      | The library page features a title "Library" and 3 buttons underneath linking to the references, with more to come in the future. The search bar is also showcased, linking the prompts to the reference pages. If the input doesn't exist or is typed wrong, it showcases a new page displaying the "Search Results," then a link underneath routing to the Library, while the text "More References Coming Soon..." is shown underneath, and if there is no input, the same is shown; however, the text is instead replaced with "Please enter a search term".                                                                                |
| **Gif**  | Responsive Demo ![Ani-Basics](/docs/gif/Adaptability.gif)                                      |
| **Description**      | The responsive demo demonstrates the website's adaptability to different screen sizes.                                                                                     |

**Your walkthrough should show:**

- A tour of each page (Home and Contact)
- Your key Bootstrap components working (navbar, carousel, cards, map, form)
- The layout responding when the window is resized (navbar collapsing to a hamburger)

---

## 3. Evaluation — Did You Deliver Your Statement of Intent?
This is the most important written part of your documentation. Evaluate the
website you **delivered** against the **Statement of Intent** you wrote during
planning. Be honest and use evidence — point to a page, a feature or a test.
### 3.1 Your Statement of Intent

What is the website?
Ani-Ref is an educational animation reference resource website dedicated for animators needing references for their animations. The site will include a home page, with a button that when pressed, leads to an array of references featuring angles,  positions and movements of photos,  and videos with the user's intended topic, organised alphabetically.

Why is it needed? (The problem)
Currently many animators (beginners or even experts)lack the resources of even basic topics like, for example; how an animal looks through this angle, position, or its movement. Animators have to spend time searching through countless photos and videos of references that seem impossible to find. All of these countless hours,wasted when,could be used more efficiently.

Why is it needed? (The solution)
By creating a dedicated website, with countless of references and resources, all organised and clear to see, and user interfaces like a search bar,and buttons linking resources.We can solve issues of inefficiency, searching the web, for the price of nothing, while being an educational website teaching others, as a result. Planning the solution in this way , before any design or development begins, ensures the website is purposeful, cohesive and genuinely useful from launch day.

Who is it for?
The primary audience are young animators from any skill level, primarily ages 13-18, looking for an educational website  for animation and a collection of easy to access references,so the site must be quick to navigate. Knowing our audience in advance allows every design and content decision to be made with real users in mind, which is fundamental to  delivering a website that people will actually want to use.

Summary
Ani-Ref will transform young beginner animators workflow,fueled with easy to access references. With a home page, search bar and buttons linking resources we expect to solve the inefficiency of finding resources or references on your own.This outcome is only achievable because we took the time  to plan carefully, identifying the purpose, the audience, and the features before building anything, laying the foundation for a website that is both high quality and fit for purpose.

### 3.2 What You Delivered

| Page    | Route      | What it delivers |
| ------- | ---------- | ---------------- |
| Home    | `/home`    | Homepage with a title, navigation bar and carousel linking to the contact, library and ani-basics page, and a footer underneath with navigation links and "About us" section.                |
| Contact | `/contact` | Contact page with a title and query Card for any questions viewers might have and a footer underneath.                |
| Ani-Basics | `/anibasics` | Contact page with a tile and 12 video cards with descriptions underneath and a footer underneath.                |
| Library | `/library` | Library page with a title and buttons of the references (animals, people and, nature).                 |
| Animals | `/animals` | Animals page with 4 videos displaying the refernece and a short description underneath it.                 |
| Nature | `/nature` | Nature page with 4 videos displaying the refernece and a short description underneath it.                |
| People | `/people` | People page with 4 videos displaying the refernece and a short description underneath it.                 |
### 3.3 Evaluation Against Your Intent (2–3 paragraphs)

> Take each aim in your Statement of Intent and evaluate **how well the
> delivered site meets it**. Where did you meet your intent? Where did you fall
> short, and why? Support every judgement with evidence from your site.

The website aimed to be an organised, easy-to-navigate educational reference resource that improves animator workflow and solves the problem of inefficient reference searching. Overall, the delivered site reasonably well meets the aim through its clear layout and intuitive navigation.

This can be seen on the homepage. The carousel and navigation bar provide quick access to the three most important pages (Library, Ani-Basics and Contact). At the same time, the footer consistently appears across all pages and offers a short, sharp "About Us" section and links to said three most important pages. A readable font, aesthetic text styling, and smooth card transitions were added, improving the site's overall effectiveness. All of these features optimise the site's navigation and overall aim of improving animator workflow, reducing the time spent on resources, and optimising its effectiveness.

However, this aim is only partially met as the site currently lacks a wide range of references. The categories provided are broad and limited, such as animals, people, and nature. This means the site does not yet fully solve the problem of inefficient searching.

### 3.4 Overall Effectiveness (1–2 paragraphs)

> Step back from the detail. Overall, **how effective** is the website at
> achieving its purpose for its target audience? Weigh what works against what
> falls short, and state what you would improve to better meet your intent.

<!-- Write 1–2 paragraphs. -->
Overall, the website is largely effective at achieving its purpose. It is an educational reference resource for young animators. The clear navigation bar, carousel, and consistent footer make the site easy to browse through, which supports the target audience's need for quick access to reference material. The simple layout and direct descriptions support younger users who benefit from straightforward interfaces.

The most significant improvement would be expanding the reference library with more specific and diverse categories. If the broad, limited references were improved as said, the site's usefulness could ultimately solve the problem of inefficient searching. Increasing the number of high-quality references would make the site more effective for its intended audience.

---

## 4. Acknowledgements

> List anything you did not make yourself — tutorials, images, fonts, icons and
> libraries. Using content without acknowledgement may constitute academic
> misconduct.

| What you used | Source / Creator | Licence | What you used it for   |
| ------------- | ---------------- | ------- | ---------------------- |
| Bootstrap     | Bootstrap team   | MIT     | Layout and components  |
| Flask         | Pallets Projects | BSD     | Web server and routing |
| Youtube           | Youtube (Alan Becker)                 | N/a      | 12 principle of animation videos and explanation                    |
| Google Fonts  | Fonts                 | 	SIL Open Fonts License        | Text in Ani-Basics and icons                       |
| Research Gate|  Preston Blair  | Fair Use (Educational) | Hero image carousel and contact page|

---

> **Student Declaration:** All work submitted is my own except where explicitly acknowledged above.
