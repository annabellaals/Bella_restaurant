// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// isotope js
$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

// nice select
// $(document).ready(function () {
//     $('select').niceSelect();
// });

/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});


function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}


function appendObjectToLocalStorage(obj) {
    let array = JSON.parse(localStorage.getItem("bella_cart")) || [];
    const index = array.findIndex(item => item.id === obj.id);
    if (index === -1) {
        array.push(obj);
    }
    localStorage.setItem("bella_cart", JSON.stringify(array));
    document.getElementById(`cart_add_button-${obj.id}`).innerHTML = `<i class="fa-solid fa-check"></i>`
}


function getItems() {
    const items = JSON.parse(localStorage.getItem('bella_cart')) || [];
    displayItems(items)
}

function deleteItems(id) {
    console.log(id)
    let array = JSON.parse(localStorage.getItem('bella_cart')) || [];
    const index = array.findIndex(item => item.id === id);
    if (index !== -1) {
        array.splice(index, 1);
    }
    localStorage.setItem('bella_cart', JSON.stringify(array));
    displayItems(array)
}

function displayItems(items) {
    const container = document.getElementById('itemsContainer');
    container.innerHTML = '';
    let total_price = 0
    items.forEach(item => {
        const itemDiv = ` <div class="card mb-3">
                        <div class="card-body">
                            <div class="d-flex justify-content-between">
                                <div class="d-flex flex-row align-items-center">
                                    <div>
                                        <img
                                                src="${item.image_url}"
                                                class="img-fluid rounded-3" alt="Shopping item" style="width: 65px;">
                                    </div>
                                    <div class="ms-3" style="margin-left: 20px">
                                        <h5>${item.name}</h5>
                                        <p class="small mb-0">${item.description}</p>
                                    </div>
                                </div>
                                <div class="d-flex flex-row align-items-center">
                                    <div style="width: 50px;">
                                        <h5 class="fw-normal mb-0">1</h5>
                                    </div>
                                    <div style="width: 80px;">
                                        <h5 class="mb-0">$ ${item.price}.00</h5>
                                    </div>
                                    <span style="color: #cecece;margin-left: 20px;cursor: pointer" onclick='deleteItems("${item.id}")'><i class="fa-solid fa-xmark"></i></span>
                                </div>
                            </div>
                        </div>
                    </div>`
        container.innerHTML += itemDiv;
        total_price += item.price
    });
    const elements = document.querySelectorAll('.total_price_display');
    elements.forEach(element => {
        element.innerText = `$${total_price}.00`
    });
}

function place_order(is_authenticated) {
    if (is_authenticated === "False")
        window.location.href = "/login?next=/cart"
    const array = JSON.parse(localStorage.getItem("bella_cart")) || [];
    if (array.length === 0)
        return

    const ids = array.map(item => item.id);
    $.ajax({
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        type: "POST",
        url: "ajax/place_order/",
        dataType: 'json',
        contentType: "application/json",
        data: JSON.stringify({
            item_ids: ids,
        }),
        success: function (data) {
            localStorage.setItem('bella_cart', JSON.stringify([]));
            window.location.href = data.redirect
        },
        failure: function (data) {
            console.log(data)
        }
    });
}

window.onload = getItems;

const datePicker = document.getElementById('date-picker');
const timePicker = document.getElementById('time-picker');

const now = new Date();
const today = now.toISOString().split('T')[0];

// Set minimum date to today
datePicker.setAttribute('min', today);
datePicker.value = today;

const formatTime = (hour, minute) => {
    const ampm = hour >= 12 ? 'PM' : 'AM';
    const formattedHour = hour % 12 || 12; // Convert 24-hour to 12-hour format
    const formattedMinute = minute < 10 ? '0' + minute : minute;
    return `${formattedHour}:${formattedMinute} ${ampm}`;
};

const addTimeOption = (hour, minute) => {
    const timePicker = document.getElementById('time-picker');
    const option = `<option value="${formatTime(hour, minute)}">${formatTime(hour, minute)}</option>`
    timePicker.innerHTML += option;
};

const generateTimeOptions = (startHour, startMinute, endHour = 23, endMinute = 30) => {
    const timePicker = document.getElementById('time-picker');
    timePicker.innerHTML = ''; // Clear existing options
    for (let hour = startHour; hour <= endHour; hour++) {
        const startMins = (hour === startHour) ? startMinute : 0;
        const endMins = (hour === endHour) ? endMinute : 30;
        for (let minute = startMins; minute <= endMins; minute += 30) {
            addTimeOption(hour, minute);
        }
    }
};

const updateTimeOptions = () => {
    const selectedDate = new Date(datePicker.value);
    if (selectedDate.toISOString().split('T')[0] === today) {
        const currentHour = now.getHours();
        const currentMinute = now.getMinutes();
        const roundedMinutes = Math.round(currentMinute / 30) * 30;
        generateTimeOptions(currentHour >= 14 ? currentHour: 14, currentHour >= 14 ? roundedMinutes: 0 );
    } else {
        generateTimeOptions(14, 0);
    }
};

// Initialize time options
updateTimeOptions();

// Update time options when date changes
datePicker.addEventListener('change', updateTimeOptions);

function checkAvailability() {
    const datePicker = document.getElementById('date-picker');
    const timePicker = document.getElementById('time-picker');
    var dateValue = datePicker.value;
    var timeValue = timePicker.value;

    $.ajax({
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        type: "POST",
        url: 'ajax/check-table-availability/',
        dataType: 'json',
        contentType: "application/json",
        data: JSON.stringify({
            date_value: dateValue,
            time_value: timeValue
        }),
        success: function (data) {
            if (data && data.response) {
                const container = document.getElementById('table_row');
                container.innerHTML = '';
                if (data.tables.length) {
                    document.getElementById('table-title').innerText = "Select Table";
                }
                data.tables.forEach(item => {
                    let itemDiv = ""
                    if (item.is_available)
                        itemDiv = `<div style="display: flex;align-items: center;gap: 10px;">
                                <div class="table-icon table-icon-hover" style="padding:3px" onclick="toggleTableSelection(this)" id="${item.table_id}">
<img src="/static/images/table.png" alt="" style="width: 100%;height: 100%;object-fit: cover;object-position: center;"/>
</div>
                                 ${item.table_id}
                            </div>`
                    else
                        itemDiv = `<div style="display: flex;align-items: center;gap: 10px;">
                                <div class="table-icon"  style="padding:3px">
<img src="/static/images/table.png" alt="" style="width: 100%;height: 100%;object-fit: cover;object-position: center;"/>

</div>
                                 ${item.table_id} (booked)
                            </div>`
                    container.innerHTML += itemDiv;
                });
            }
        },
        failure: function (data) {
            console.log(data)
        }
    });
}
