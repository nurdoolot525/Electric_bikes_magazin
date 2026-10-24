const burgerBtn = document.querySelector('.burger_icon');
const burgerMenu = document.querySelector('.burger-menu');   
const mobileMenu = document.querySelector('.mobile-menu');   

if (burgerBtn) {
    burgerBtn.addEventListener('click', () => {
        if (window.innerWidth <= 850) {
            mobileMenu.classList.add('active');
        } else {
            burgerMenu.classList.add('active');
        }
    });
}

const closeBtn = document.querySelector('.close_btn');
if (closeBtn) {
    closeBtn.addEventListener('click', () => {
        burgerMenu.classList.remove('active');
    });
}

const mobileMenuClose = document.querySelector('.mobile-menu-close');
if (mobileMenuClose) {
    mobileMenuClose.addEventListener('click', () => {
        mobileMenu.classList.remove('active');
    });
}

document.querySelectorAll('.mobile-item-title').forEach((title) => {
    title.addEventListener('click', () => {
        const item = title.parentElement;
        item.classList.toggle('open');
    });
});



const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
const bikesCards = document.querySelector('.bikes_cards');

if (nextBtn && bikesCards) {
    nextBtn.addEventListener('click', () => {
        bikesCards.scrollBy({ left: 380, behavior: 'smooth' });
    });
}

if (prevBtn && bikesCards) {
    prevBtn.addEventListener('click', () => {
        bikesCards.scrollBy({ left: -380, behavior: 'smooth' });
    });
}

function uncheckOthers(current) {
    const checkboxes = document.querySelectorAll(`input[name="${current.name}"]`);
    checkboxes.forEach((cb) => {
        if (cb !== current) {
            cb.checked = false;
        }
    });
    current.form.submit();
}


function changeSort(value) {
    const url = new URL(window.location.href);
    url.searchParams.set('sort', value);
    window.location.href = url.toString();
}

const filterToggleBtn = document.querySelector('.filter_toggle_btn');
const filtersPanel = document.querySelector('.filters');
const filtersOverlay = document.querySelector('.filters_overlay');
const filtersClose = document.querySelector('.filters_close');

if (filterToggleBtn && filtersPanel && filtersOverlay) {
    filterToggleBtn.addEventListener('click', () => {
        filtersPanel.classList.add('active');
        filtersOverlay.classList.add('active');
    });
}

if (filtersClose && filtersPanel && filtersOverlay) {
    filtersClose.addEventListener('click', () => {
        filtersPanel.classList.remove('active');
        filtersOverlay.classList.remove('active');
    });
}

if (filtersOverlay && filtersPanel) {
    filtersOverlay.addEventListener('click', () => {
        filtersPanel.classList.remove('active');
        filtersOverlay.classList.remove('active');
    });
}


const eqPrevBtn = document.querySelector('.eq_prev');
const eqNextBtn = document.querySelector('.eq_next');
const eqCards = document.querySelector('.eq_cards');

if (eqNextBtn && eqCards) {
    eqNextBtn.addEventListener('click', () => {
        eqCards.scrollBy({ left: 385, behavior: 'smooth' });
    });
}

if (eqPrevBtn && eqCards) {
    eqPrevBtn.addEventListener('click', () => {
        eqCards.scrollBy({ left: -385, behavior: 'smooth' });
    });
}


function setMainImage(el) {
    document.getElementById('mainImage').src = el.src;
    document.querySelectorAll('.thumb').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
}

function selectOption(el) {
    el.parentElement.querySelectorAll('button, .color_dot').forEach(o => o.classList.remove('active'));
    el.classList.add('active');
}

let qty = 1;
function changeQty(diff) {
    qty = Math.max(1, qty + diff);
    document.getElementById('qtyValue').textContent = qty;
}


const similarPrevBtn = document.querySelector('.similar_prev');
const similarNextBtn = document.querySelector('.similar_next');
const similarCards = document.querySelector('.similar_cards');

if (similarNextBtn && similarCards) {
    similarNextBtn.addEventListener('click', () => {
        similarCards.scrollBy({ left: 300, behavior: 'smooth' });
    });
}

if (similarPrevBtn && similarCards) {
    similarPrevBtn.addEventListener('click', () => {
        similarCards.scrollBy({ left: -300, behavior: 'smooth' });
    });
}