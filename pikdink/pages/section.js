const content = require('../services/content')

module.exports = function sectionPage(id) {
  const section = content.sections.find(item => item.id === id)
  const items = content.list(id)
  const categories = [...new Set(items.map(item => item.category))]

  return {
    data: { section, items, categories, activeCategory: '' },
    selectCategory(event) {
      const category = event.currentTarget.dataset.category
      this.setData({
        activeCategory: category,
        items: category ? items.filter(item => item.category === category) : items,
      })
    },
  }
}
