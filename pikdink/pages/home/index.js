const content = require('../../services/content')

Page({
  data: {
    sections: content.sections,
    featured: content.get('first-game'),
    items: content.list().filter(item => item.id !== 'first-game'),
  },
})
