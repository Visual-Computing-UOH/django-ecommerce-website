'use strict';

/**
 * OVERLAY
 */
const overlay = document.querySelector('[data-overlay]');

/**
 * MOBILE MENU / SIDEBAR TOGGLE
 * (covers header hamburger menu AND product-page sidebar filter,
 *  since both use the same data-mobile-menu attribute)
 */
const mobileMenuOpenBtns = document.querySelectorAll('[data-mobile-menu-open-btn]');
const mobileMenus = document.querySelectorAll('[data-mobile-menu]');
const mobileMenuCloseBtns = document.querySelectorAll('[data-mobile-menu-close-btn]');

const mobileMenuToggler = function () {
  mobileMenus.forEach(menu => menu.classList.toggle('active'));
  if (overlay) overlay.classList.toggle('active');
};

mobileMenuOpenBtns.forEach(btn => btn.addEventListener('click', mobileMenuToggler));
mobileMenuCloseBtns.forEach(btn => btn.addEventListener('click', mobileMenuToggler));
if (overlay) overlay.addEventListener('click', mobileMenuToggler);

/**
 * ACCORDION (used in mobile menu categories and sidebar filters)
 */
const accordionBtns = document.querySelectorAll('[data-accordion-btn]');

accordionBtns.forEach(btn => {
  btn.addEventListener('click', function () {
    this.classList.toggle('active');
    const panel = this.nextElementSibling;
    if (panel) panel.classList.toggle('active');
  });
});

/**
 * NOTIFICATION TOAST CLOSE (if any toast-like element exists elsewhere)
 */
const toastCloseBtns = document.querySelectorAll('[data-toast-close]');
toastCloseBtns.forEach(btn => {
  btn.addEventListener('click', function () {
    const toast = this.closest('[data-toast]');
    if (toast) toast.classList.remove('active');
  });
});

/**
 * MODAL CLOSE (if any modal-like element exists elsewhere)
 */
const modalCloseBtns = document.querySelectorAll('[data-modal-close], [data-modal-overlay]');
modalCloseBtns.forEach(btn => {
  btn.addEventListener('click', function () {
    const modal = this.closest('[data-modal]');
    if (modal) modal.classList.remove('active');
  });
});
