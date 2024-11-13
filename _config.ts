import lume from "lume/mod.ts"
import jsx_preact from "lume/plugins/jsx_preact.ts"
import code_highlight from "lume/plugins/code_highlight.ts"
import mdx from "lume/plugins/mdx.ts"
import tailwindcss from "lume/plugins/tailwindcss.ts"
import postcss from "lume/plugins/postcss.ts"

const site = lume({
    src: "./src",
})

site.use(jsx_preact())
site.use(code_highlight())
site.use(mdx())
site.use(tailwindcss({
    extensions: [".html", ".tsx"],
    // @ts-ignore false error
    options: {
        corePlugins: {
            preflight: false,
        },
    },
}))
site.use(postcss())

site.copy("public")

export default site
