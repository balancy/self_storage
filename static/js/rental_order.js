const allStorages = JSON.parse(document.getElementById('all_storages').textContent);
const allPromocodes = JSON.parse(document.getElementById('all_promocodes').textContent);

const today = new Date().toISOString().slice(0, 10)

const discountEl = document.querySelector("#discount");
const discountLabelEl = document.querySelector("#discount_label");
const durationEl = document.querySelector("#duration");
const sizeEl = document.querySelector("#size");
const storageEl = document.querySelector("#storage");
const promocodeEl = document.querySelector("#promocode");
const totalPriceEl = document.querySelector("#total_price");
const totalPriceLabelEl = document.querySelector("#total_price_label");

[storageEl, sizeEl, durationEl].forEach(item => {
    item.addEventListener('change', event => {
        calculateTotalPrice();
    })
})

let currentDiscount = 0;
let totalPrice = 0;

const calculateTotalPrice = () => {
    let currentStorage = allStorages[storageEl.value];
    let size = sizeEl.value;

    if (currentStorage && size != 0) {
        let basePrice = currentStorage.base_price;
        let additionalPrice = currentStorage.additional_price;
        let duration = durationEl.value;

        totalPrice = Math.ceil((1 - currentDiscount / 100) * duration *
            (+basePrice + +additionalPrice * (size - 1)))
    }
    else {
        totalPrice = 0
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