const content = require('../../services/content')

Page({
  data: { query: '', items: [] },

  updateQuery(event) {
    const query = event.detail.value
    this.setData({ query, items: content.search(query), hasQuery: Boolean(query.trim()) })
  },
})
