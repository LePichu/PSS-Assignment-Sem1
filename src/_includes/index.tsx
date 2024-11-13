import { JSX } from "npm:preact@10.24.3"

interface Props {
    children: JSX.Element
}

export default function Layout(props: Props) {
    return (
        <>
            <html>
                <head>
                    <link rel="stylesheet" href="/index.css"></link>
                </head>
                <body>
                    <header class="flex flex-row justify-between items-center p-4">
                        <img src="/public/Chitkara_Logo_Color.png" class="h-16 w-16"></img>
                        <h1 class="flex-grow">Problem Solving Skills - 24CS007</h1>
                    </header>
                    <main>
                        {props.children}
                    </main>
                </body>
            </html>
        </>
    )
}
