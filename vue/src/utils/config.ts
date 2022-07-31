export interface Env {
  TITLE: string
}

export default (function load(): Promise<Env> {
  return fetch('config.json').then(res => res.json()).then(res => {
    return res
  })
});