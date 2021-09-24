extentions =[
'brettlempereur.theme-base16grayscale',
'CoenraadS.bracket-pair-colorizer-2',
'dbaeumer.vscode-eslint',
'dracula-theme.theme-dracula',
'dsznajder.es7-react-js-snippets',
'formulahendry.auto-rename-tag',
'humao.rest-client',
'joelday.docthis',
'mjmcloug.vscode-elixir',
'ms-toolsai.jupyter',
'ms-vsliveshare.vsliveshare',
'PKief.material-icon-theme',
'Prisma.prisma',
'ritwickdey.LiveServer',
'streetsidesoftware.code-spell-checker',
'streetsidesoftware.code-spell-checker-portuguese-brazilian',
'Tyriar.sort-lines',
'wmaurer.vscode-jumpy',
'xabikos.JavaScriptSnippets',
]

for extension in extensions:
    do code --install-extension $extension
done