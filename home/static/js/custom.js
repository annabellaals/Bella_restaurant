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
$(document).ready(function () {
    $('select').niceSelect();
});

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