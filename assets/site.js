/* Progressive enhancement: the portfolio and all projects remain readable without JS. */
(() => {
  const controls = document.querySelector('[data-filter-ui]');
  if (!controls) return;
  const cards = Array.from(document.querySelectorAll('[data-category]'));
  const search = document.querySelector('#project-search');
  const count = document.querySelector('.project-count');
  const empty = document.querySelector('#no-results');
  const buttons = Array.from(document.querySelectorAll('[data-filter]'));
  let category = 'All projects';
  function update() {
    const query = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    for (const card of cards) {
      const matches = (category === 'All projects' || card.dataset.category === category) && card.textContent.toLocaleLowerCase().includes(query);
      card.hidden = !matches;
      if (matches) visible++;
    }
    count.textContent = `${visible} ${visible === 1 ? 'project' : 'projects'}`;
    empty.hidden = visible !== 0;
  }
  for (const button of buttons) button.addEventListener('click', () => {
    category = button.dataset.filter;
    for (const other of buttons) other.setAttribute('aria-pressed', String(other === button));
    update();
  });
  search.addEventListener('input', update);
  controls.hidden = false;
})();
