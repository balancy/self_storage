const allItems = JSON.parse(document.getElementById('all_items').textContent);
const allPromocodes = JSON.parse(document.getElementById('all_promocodes').textContent);

const today = new Date().toISOString().slice(0, 10)

const discountEl = document.querySelector("#discount");
const discountLabelEl = document.querySelector("#discount_label");
const durationEl = document.querySelector("#duration");
const itemDetailsEl = document.querySelector("#item_details");
const itemEl = document.querySelector("#item");
const itemImageEl = document.querySelector("#item_img");
const itemPriceDetailsEl = document.querySelector("#item_price_details");
const quantityEl = document.querySelector("#quantity");
const promocodeEl = document.querySelector("#promocode");
const totalPriceEl = document.querySelector("#total_price");
const totalPriceLabelEl = document.querySelector("#total_price_label");

[itemEl, quantityEl, durationEl].forEach(item => {
    item.addEventListener('change', event => {
        updateItemDetais();
    })
})

let currentDiscount = 0;
let totalPrice = 0;
let currentItem;
let weekPrice;
let monthPrice;

const calculateTotalPrice = () => {
    currentItem = allItems[itemEl.value];

    if (currentItem) {
        weekPrice = currentItem.week_storage_price;
        monthPrice = currentItem.month_storage_price;
        let duration = durationEl.value;
        let quantity = quantityEl.value;

        totalPrice = duration < 4
            ? Math.ceil((1 - currentDiscount / 100) * quantity * duration * weekPrice)
            : Math.ceil((1 - currentDiscount / 100) * quantity * Math.floor(duration / 4) * monthPrice)
    } else {
        totalPrice = 0;
    }

    totalPriceLabelEl.innerHTML = totalPrice;
    totalPriceEl.value = totalPrice;
}

const checkPromocode = () => {
    let currentPromocode = allPromocodes[promocodeEl.value];

    if (currentPromocode) {
        startDate = currentPromocode.start_date;
        endDate = currentPromocode.end_date;
        isActive = today > startDate && today < endDate;

        if (isActive) {
            currentDiscount = currentPromocode.discount;
        }
    } else {
        currentDiscount = 0;
    }

    discountLabelEl.innerHTML = currentDiscount;
    discountEl.value = currentDiscount;

    calculateTotalPrice();
}

const updateItemDetais = () => {
    currentItem = allItems[itemEl.value]

    if (currentItem) {
        weekPrice = currentItem.week_storage_price;
        monthPrice = currentItem.month_storage_price;

        itemDetailsEl.style.display = 'block';
        itemImageEl.setAttribute('src', 'media/' + currentItem.image);
        itemPriceDetailsEl.innerHTML =
            'Стоимость хранения за единицу: ' + weekPrice +
            ' руб/неделю, ' + monthPrice + ' руб/месяц';
    } else {
        itemDetailsEl.style.display = 'none';
    }

    calculateTotalPrice();
}