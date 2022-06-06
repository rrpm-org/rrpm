# Contributing to RRPM

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to RRPM and its packages, which are hosted in the [pybash1 user](https://github.com/pybash1) on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Code of Conduct

This project and everyone participating in it is governed by the [RRPM Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to pybash#3122 on our discord server.

## I don't want to read this whole thing I just have a question!!!

> **Note:** Please don't file an issue to ask a question. You'll get faster results by using the resources below.
We have an official message board with a discord server and where the community chimes in with helpful advice if you have questions.

* [GitHub Discussions, the official RRPM message board](https://github.com/pybash1/RRPM/discussions)
* [Discord Server](https://discord.gg/FwsGkZAqcZ)

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for RRPM. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating bug reports, please check [this list](#before-submitting-a-bug-report) as you might find out that you don't need to create one. When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-a-good-bug-report). Fill out the required template, the information it asks for helps us resolve issues faster.

> **Note**: If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.
#### Before Submitting A Bug Report

* **Check the [documentation](https://pybash.gitbook.io/rrpm)** for tips — you might discover that the enhancement is already available. Most importantly, check if you're using the latest version of RRPM.
* **Check the [discussions](https://github.com/pybash1/RRPM/discussions)** for a list of common questions and problems.
* **Perform a cursory search** to see if the problem has already been reported. If it has **and the issue is still open**, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue on that repository and provide the following information by filling in the template.

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. For example, start by explaining how you started RRPM, e.g. which command exactly you used in the terminal, or how you started RRPM otherwise. When listing steps, **don't just say what you did, but explain how you did it**. For example, if you moved the cursor to the end of a line, explain if you used the mouse, or a keyboard shortcut or an RRPM command, and if so which one?
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/paste able snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem. If you use the keyboard while following the steps, **record the GIF with the [Keybinding Resolver](https://github.com/RRPM/keybinding-resolver) shown**. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.

Provide more context by answering these questions:

* **Did the problem start happening recently** (e.g. after updating to a new version of RRPM) or was this always a problem?
* If the problem started happening recently, **can you reproduce the problem in an older version of RRPM?** What's the most recent version in which the problem doesn't happen? You can download older versions of RRPM from [the releases page](https://github.com/RRPM/RRPM/releases).
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.

Include details about your configuration and environment:

* **Which version of RRPM are you using?** You can get the exact version by running `RRPM -v` in your terminal
* **What's the name and version of the OS you're using**?
* **Are you running RRPM in a virtual machine?** If so, which VM software are you using and which operating systems and versions are used for the host and the guest?
* **Are you using RRPM with multiple monitors?** If so, can you reproduce the problem when you use a single monitor?
* **Which keyboard layout are you using?** Are you using a US layout or some other layout?

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for RRPM, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion :pencil: and find related suggestions :mag_right:.

Before creating enhancement suggestions, please check [this list](#before-submitting-an-enhancement-suggestion) as you might find out that you don't need to create one. When you are creating an enhancement suggestion, please [include as many details as possible](#how-do-i-submit-a-good-enhancement-suggestion). Fill in [the template](https://github.com/RRPM/.github/blob/master/.github/ISSUE_TEMPLATE/feature_request.md), including the steps that you imagine you would take if the feature you're requesting existed.

#### Before Submitting An Enhancement Suggestion

* **Check the [documentation](https://pybash.gitbook.io/rrpm)** for tips — you might discover that the enhancement is already available. Most importantly, check if you're using the latest version of RRPM.
* **Check if there's already an extension which provides that enhancement.**
* **Perform a cursory search** to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue in the repository and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include copy/paste able snippets which you use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Include screenshots and animated GIFs** which help you demonstrate the steps or point out the part of RRPM which the suggestion is related to. You can use [this tool](https://gifcap.dev) to record GIFs.
* **Explain why this enhancement would be useful** to most RRPM users and isn't something that can or should be implemented as a community extension.
* **List some other tools or applications where this enhancement exists.**
* **Specify which version of RRPM you're using.** You can get the exact version by running `RRPM -v` in your terminal
* **Specify the name and version of the OS you're using.**

### Your First Code Contribution

Unsure where to begin contributing to RRPM? You can start by looking through these `good-first-issue` and `help-wanted` issues:

* [Good first issues][good-first-issue] - issues which should only require a few lines of code, and a test or two.
* [Help wanted issues][help-wanted] - issues which should be a bit more involved than `beginner` issues.

Both issue lists are sorted by total number of comments. While not perfect, number of comments is a reasonable proxy for impact a given change will have.

If you want to read about using RRPM or developing extensions for RRPM, the [RRPM Documentation](https://pybash.gitbook.io/rrpm) is free and available online.

#### Local development

RRPM  can be developed locally. RRPM requires Oython 3.7 or newer and [Poetry](https://python-poetry.org).

### Pull Requests

The process described here has several goals:

- Maintain RRPM's quality
- Fix problems that are important to users
- Engage the community in working toward the best possible RRPM
- Enable a sustainable system for RRPM's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Follow all instructions in [the template](PULL_REQUEST_TEMPLATE.md)
2. Follow the [styleguide](#styleguide)
3. After you submit your pull request, verify that all [status checks](https://help.github.com/articles/about-status-checks/) are passing <details><summary>What if the status checks are failing?</summary>If a status check is failing, and you believe that the failure is unrelated to your change, please leave a comment on the pull request explaining why you believe the failure is unrelated. A maintainer will re-run the status check for you. If we conclude that the failure was a false positive, then we will open an issue to track that problem with our status check suite.</details>

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

## Styleguide

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or fewer
* Reference issues and pull requests liberally after the first line
* Consider following [conventional commit messages](https://conventionalcommits.org)
