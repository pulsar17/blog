Switching my editor to (neo)?vim 🗒️
####################################

:date: 2021-10-31 02:58
:modified: 2021-10-31 02:58
:tags: vim, neovim, editor
:category: Tools
:slug: why-neo-vim
:authors: Ishaan Arora
:summary: VSCodium started to feel boring

My old editor setup
**************************************
I've used `VSCodium <https://vscodium.com/>`_ as my editor since the beginning of my programming career. Reasons for using it were - popularity, ease of using extensions, integrated terminal, but mostly because it was the first editor I used. After a while I switched to the *vim* extension for all my editing needs. I did that because I wasn't satisfied with the editing experience inside VSCodium and I also wanted to learn vim.

I used VSCodium with the vim extension throughout my `GSoC <{filename}/fourth.rst>`_ program. It is a good extension but I bumped into its limitations fairly quickly. For example, the ``:norm`` command did not work in the extension, sometimes the vim shortcuts and VSCodium shortcuts clashed which got very annoying after a while.

In September, I decided that I wanted to leave VSCodium and completely move to vim. Why settle for a sub-par vim experience when I could use the classic editor itself?

My not so old editor setup - A transition phase
************************************************
I successfully did it, I switched to vim 💯 

It was surprising to me how much an editor could be configured.

I added all the good extensions, configured exactly the whitespace characters I wanted to see, and even ``noremap`` mapped some of the mappings.

This time too, I bumped into some limitations but this time these were limitations of vim. Yes folks, vim is not the omnipotent program that has the answer to everything. Also, and this might sound a bit silly, but vim is a great **editor**, but not so much as a great IDE [#digress]_.🤯  (Shocker right?)

More precisely, vim has limited support for intellisense [#out]_. It has no built-in debugger [#out]_.
I used vim for around 2 weeks but I didn't write any serious programs that required a debugger.

After dabbling in some Reddit threads I decided to try `neovim <https://neovim.io/>`_. It's a fork of vim that aims to be a better out of the box experience. The feature I was most excited about in neovim was native LSP [#lsp]_ support. LSP, at its simplest is a separation of the language specific features like linting, autocompletion in a separate server with the editor acting as a client. This allows for an abstraction for the editor so that it can focus on what it does best - *editing*. neovim provides a native LSP client. A language server still needs to be installed though, the complexity of which varies by language. For Python, there are two language servers that are officially supported, ``pylsp`` and ``pyright`` [#pyright]_. Both of these servers are available under an Open Source License.

Setting up these servers was not trivial. It was confusing as the configuration language for these servers is Lua. It's a very good language, feels very light, but I hadn't learned it at that point. I also had no idea how various pieces were going to fit together. In VSCodium, it's a one-click install, simple. That being said, I took this as an opportunity to learn about the tooling. VSCodium did not provide this opportunity as it obscures these details.

My current setup
****************

My current setup uses neovim with a majestic ~150 line ``.vimrc`` and a beautiful ~200 line ``init.vim``. I mostly write Python, so I have pylsp and pyright installed. The only thing I miss in neovim is the native debugger support like LSP. There is an extension that implements the DAP [#dap]_ but I haven't looked into it much (I couldn't figure out how to make it work when I used it). I hope that DAP support in neovim will mature over time and feel like a more coherent and integrated experience.

I am extremely satisfied with the editing experience inside neovim. I even learned the basics of Lua and wrote a plugin to help with a very specific task in Django. I'll write a separate article about the experience of writing a Lua plugin and various roadblocks, issues, problems I faced while writing it.

For now, here are my latest ``.vimrc`` and ``init.vim``.

📎 `.vimrc <{attach}/files/vimrc>`_

📎 `init.vim <{attach}/files/init.vim>`_

*I will replace these resource links with the version controlled resource links if and when I create my dotfiles repo.*

.. rubric:: **Footnotes**
.. [#digress] This is definitely true for Python. I am not much experienced with vim for other languages, but its workflow feels optimized towards compiled (C family) languages given its lineage.
.. [#out] Out of the box without any extensions.
.. [#pyright] Pyright is the language server that VSCode used for its Python extension. As of writing this article, it has been replaced by a `proprietary server <https://github.com/microsoft/pylance-release/issues/4>`_ Pylance.
.. [#lsp] LSP stands for Language Server Protocol. https://langserver.org/ has more verbose explanation about its need. The website also maintains a list of implementations for various languages.
.. [#dap] DAP stands for Debug Adapter Protocol. An analogue of LSP for Debuggers.
