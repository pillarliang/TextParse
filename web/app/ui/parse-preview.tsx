import {marked} from 'marked'
import sanitizeHtml from 'sanitize-html'

const allowedTags = sanitizeHtml.defaults.allowedTags.concat([
  'img',
  'h1',
  'h2',
  'h3',
])
const allowedAttributes = Object.assign(
  {},
  sanitizeHtml.defaults.allowedAttributes,
  {
    img: ['alt', 'src'],
  }
)


export default function NotePreview({ children }: any) {
  return (
    <div className="note-preview text-with-markdown">
      <div
        dangerouslySetInnerHTML={{
          __html: sanitizeHtml(String(marked(children || '')), {
            allowedTags,
            allowedAttributes
          })
        }}
      />
    </div>
  )
}
