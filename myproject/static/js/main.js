// boots
document.getElementById("offcan_in").addEventListener("click", function () {
  var offcanMain = document.getElementById("offcan_main");
  offcanMain.classList.toggle("show");
});

document.getElementById("offcan_off").addEventListener("click", function () {
  var offcanMain = document.getElementById("offcan_main");
  offcanMain.classList.remove("show");
});
// SEARCH
$("#show_count").click(function () {
  $("#show_count_show").toggleClass("show");
}),
  $("#show_sort").click(function () {
    $("#show_sort_show").toggleClass("show");
  }),
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".copy-button").forEach(function (e) {
      e.addEventListener("click", function () {
        var e = this.getAttribute("data-clipboard-target"),
          t = document.querySelector(e),
          r = document.createRange();
        r.selectNode(t),
          window.getSelection().removeAllRanges(),
          window.getSelection().addRange(r);
        try {
          document.execCommand("copy");
        } catch (a) {
          alert("Ошибка копирования: ", a);
        }
        window.getSelection().removeAllRanges();
      });
    });
  });
const swiper_main = new Swiper(".swiper_main", {
    loop: !0,
    slidesPerView: 1,
    // autoplay: { delay: 4e3, pauseOnMouseEnter: !0 },
    pagination: { el: ".swiper-pagination" },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    // scrollbar: { el: ".swiper-scrollbar" },
  }),
  hits_main_parent = new Swiper(".hits_main_parent", {
    // autoplay: { delay: 3e3, pauseOnMouseEnter: !0 },
    lazy: !0,
    // loop: !0,
    navigation: { nextEl: ".index-next", prevEl: ".index-prev" },
    grabCursor: !0,
    spaceBetween: 10,
    breakpoints: {
      1400: { spaceBetween: 10, slidesPerView: 4 },
      767: { spaceBetween: 10, slidesPerView: 3 },
      500: { slidesPerView: 2, loop: !0 },
      300: { slidesPerView: 1, loop: !0 },
    },
  }),
  reviews_index_main = new Swiper(".reviews_index_main", {
    autoplay: { delay: 3e3, pauseOnMouseEnter: !0 },
    lazy: !0,
    pagination: { el: ".swiper-pagination", clickable: !0 },
    navigation: { nextEl: ".arrow-next", prevEl: ".arrow-prev" },
    slidesPerView: 4,
    grabCursor: !0,
    spaceBetween: 20,
    breakpoints: {
      992: { spaceBetween: 10 },
      768: { slidesPerView: 3, spaceBetween: 10 },
      500: { slidesPerView: 2, loop: !0 },
      300: { slidesPerView: 1, loop: !0 },
    },
  }),
  headerItemDivs = document.querySelectorAll(".header_item_div_main");
headerItemDivs.forEach((e) => {
  e.addEventListener("mouseover", () => {
    e.classList.add("active");
  }),
    e.addEventListener("mouseout", () => {
      e.classList.remove("active");
    });
}),
  $(document).ready(function () {
    $(".lk_top_sign").click(function () {
      $("#authModal").toggleClass("active");
    }),
      $(".active_script").click(function () {
        $(this).toggleClass("active");
      }),
      $(".active_parent").click(function () {
        $(this).parent().toggleClass("active");
      });
  }),
  $(".primary_btn").click(function () {
    var e = $(this).attr("id").replace("-btn", ""),
      t = $("#" + e),
      r = t.hasClass("active");
    if (
      (r ||
        ($(".primary_btn").removeClass("active"), $(this).addClass("active")),
      $(".primary_desc").removeClass("active"),
      r)
    )
      t.removeClass("active"), $(this).removeClass("active");
    else {
      t.addClass("active");
      var a = $("#desc").offset().top;
      $("html, body").scrollTop(a - 80);
    }
  }),
  $(window).scroll(function () {
    var e = $(window).height(),
      t = $(window).scrollTop();
    $(".primary_desc_main").each(function () {
      var r = $(this).offset().top,
        a = $(this).outerHeight();
      t + e >= r + a - 250
        ? ($(this).addClass("active"), $(".primary_block").addClass("active"))
        : ($(this).removeClass("active"),
          $(".primary_block").removeClass("active"));
    });
  }),
  $(document).ready(function () {
    $(".btn_no").click(function () {
      $(".div_101_p").removeClass("active"),
        $(".btn_all").removeClass("active"),
        $(this).removeClass("active");
    });
  }),
  $(document).ready(function () {
    $(".write_me").click(function () {
      $("#write_me").toggleClass("active");
    });
  }),
  $(document).ready(function () {
    $(".more_review").click(function () {
      $("#review_full").toggleClass("active");
    });
  }),
  $(document).ready(function () {
    $(".close_modal").click(function () {
      $(".modal_reg").removeClass("active");
    });
  }),
  $(document).ready(function () {
    $(".review_write_btn").click(function () {
      $(".review_write").addClass("active");
    });
  });
  $(document).ready(function () {
    $(".city_btn").click(function () {
      $(".city_view").addClass("active");
    });
  });
const headerDownMain = document.querySelector(".header_down_main");
window.addEventListener("scroll", function () {
  window.pageYOffset >= 400 && !headerDownMain.classList.contains("active")
    ? headerDownMain.classList.add("active")
    : window.pageYOffset < 300 &&
      headerDownMain.classList.contains("active") &&
      headerDownMain.classList.remove("active");
}),
  $(document).ready(function () {
    $(".category_pod, .category_item").hide(),
      $(".cat_gl").click(function () {
        $(".category_pod, .category_item")
          .not($(this).nextAll(".category_pod, .category_item"))
          .slideUp(),
          $(this).next(".category_pod").slideToggle();
      }),
      $(".category_pod p").click(function () {
        $(".category_item").not($(this).next(".category_item")).slideUp(),
          $(this).next(".category_item").slideToggle();
      });
  });
// $("#writeForm").on("submit", function (e) {
//   e.preventDefault();
//   var form = $(this);
//   var url = form.attr("action");
//   var data = form.serialize();

//   $.ajax({
//     url: url,
//     type: "POST",
//     data: data,
//     success: function (response) {
//       form.trigger("reset");
//       $("#write_me").removeClass("active");
//       $("#write_ok").addClass("active");
//     },
//     error: function (response) {
//       var errors = response.responseJSON.errors;
//       var errorMessages = "";

//       // Проверяем, является ли errors объектом или строкой
//       if (typeof errors === "object") {
//         for (var field in errors) {
//           errorMessages += "<p>" + errors[field].join(", ") + "</p>";
//         }
//       } else {
//         errorMessages += "<p>" + errors + "</p>";
//       }

//       // Находим контейнер для ошибок внутри формы и обновляем его
//       var errorContainer = form.find(".error_modal");
//       errorContainer.html(errorMessages); // Обновляем поле с ошибками
//     },
//   });
// });
// $(document).ready(function () {
//   $("#review-form").on("submit", function (event) {
//     event.preventDefault();
//     var form = $(this);
//     var url = form.attr("action");
//     var data = form.serialize();

//     $.ajax({
//       url: url,
//       type: "POST",
//       data: data,
//       success: function (response) {
//         form.trigger("reset");
//         $(".review_write").removeClass("active");
//         $(".review_ok").addClass("active");
//       },

//       error: function (response) {
//         var errors = response.responseJSON.errors;
//         var errorMessages = "";

//         // Проверяем, является ли errors объектом или строкой
//         if (typeof errors === "object") {
//           for (var field in errors) {
//             errorMessages += "<p>" + errors[field].join(", ") + "</p>";
//           }
//         } else {
//           errorMessages += "<p>" + errors + "</p>";
//         }

//         // Находим контейнер для ошибок внутри формы и обновляем его
//         var errorContainer = form.find(".error_modal");
//         errorContainer.html(errorMessages); // Обновляем поле с ошибками
//       },
//     });
//   });
// });
function handleFormSubmission(formSelector, successSelector, errorSelector) {
  $(formSelector).on("submit", function (event) {
    event.preventDefault();
    var form = $(this);
    var url = form.attr("action");
    var data = form.serialize();

    $.ajax({
      url: url,
      type: "POST",
      data: data,
      success: function (response) {
        form.trigger("reset");
        $(successSelector).removeClass("active");
        $(errorSelector).addClass("active");
      },
      error: function (response) {
        var errors = response.responseJSON.errors;
        var errorMessages = "";

        // Проверяем, является ли errors объектом или строкой
        if (typeof errors === "object") {
          for (var field in errors) {
            errorMessages += "<p>" + errors[field].join(", ") + "</p>";
          }
        } else {
          errorMessages += "<p>" + errors + "</p>";
        }

        // Находим контейнер для ошибок внутри формы и обновляем его
        var errorContainer = form.find(".error_modal");
        errorContainer.html(errorMessages); // Обновляем поле с ошибками
      },
    });
  });
}
$(document).ready(function () {
  // Обработка формы для отзывов
  handleFormSubmission("#review-form", ".review_write", ".review_ok");

  // Обработка формы обратной связи
  handleFormSubmission("#writeForm", "#write_me", "#write_ok");
});

$(document).ready(function () {
  $(".show_more_review").click(function (e) {
    e.preventDefault();
    var t = $(this).data("review-id");
    $.ajax({
      url: "/reviews/get_full_review/",
      data: { review_id: t },
      success: function (e) {
        var t = e.review;
        $("#review_full .review_date").text(t.created_at),
          $("#review_full .review_name").text(t.name),
          $("#review_full .review_text").text(t.text);
      },
    });
  });
});
$(document).ready(function () {
  $(".show_more_review_product").click(function (e) {
    e.preventDefault();
    var t = $(this).data("review-id");
    $.ajax({
      url: "/reviews/get_full_review_product/",
      data: { review_id: t },
      success: function (e) {
        var t = e.review;
        $("#review_full .review_date").text(t.created_at),
          $("#review_full .review_name").text(t.name),
          $("#review_full .review_text").text(t.text);
      },
    });
  });
});

const favoriteForms = document.querySelectorAll(".favorite-form"),
  numFavoriteProductsElements = document.querySelectorAll(
    ".favorite_products_num"
  );
let num_favorite_products = parseInt(
  numFavoriteProductsElements[0].textContent
);
favoriteForms.forEach((e) => {
  e.addEventListener("submit", (t) => {
    t.preventDefault(), e.querySelector(".add-to-favorite-btn");
    let r = e.querySelector(".wish_prod"),
      a = e.getAttribute("action"),
      o = new FormData(e),
      s = r.querySelector("p");
    return (
      fetch(a, {
        method: "POST",
        body: o,
        headers: { "X-CSRFToken": "{{ csrf_token }}" },
      })
        .then((e) => e.json())
        .then((e) => {
          e.added
            ? (r.classList.add("active"),
              (num_favorite_products += 1),
              s && (s.textContent = "В избранном"))
            : (r.classList.remove("active"),
              (num_favorite_products -= 1),
              s && (s.textContent = "В избранное")),
            numFavoriteProductsElements.forEach((e) => {
              e.textContent = num_favorite_products;
            });
        })
        .catch((e) => {
          console.error(e);
        }),
      !1
    );
  });
}),
  document.addEventListener("DOMContentLoaded", function () {
    var lkTopLogin = document.querySelector("#lk_top_login");
    var loginIn = document.querySelector("#login_in");
    var timeout;

    if (lkTopLogin && loginIn) {
      lkTopLogin.addEventListener("mouseover", function () {
        // Очистить таймер, если он есть, чтобы не удалить класс при быстром наведении/уходе
        clearTimeout(timeout);
        loginIn.classList.add("active");
      });

      lkTopLogin.addEventListener("mouseleave", function () {
        // Установить таймер для удаления класса с задержкой
        timeout = setTimeout(function () {
          loginIn.classList.remove("active");
        }, 300); // 300 мс задержка перед удалением класса
      });

      loginIn.addEventListener("mouseover", function () {
        // Очистить таймер при возврате на элемент до истечения времени
        clearTimeout(timeout);
        loginIn.classList.add("active");
      });

      loginIn.addEventListener("mouseleave", function () {
        // Установить таймер для удаления класса с задержкой
        timeout = setTimeout(function () {
          loginIn.classList.remove("active");
        }, 300); // 300 мс задержка перед удалением класса
      });
    }
    // тут внес изменения
  }),
  document.addEventListener("DOMContentLoaded", function () {
    var e = document.querySelector("#lk_top_login_min"),
      t = document.querySelector("#login_in_min");

    if (e && t) {
      // Проверяем, существуют ли элементы
      e.addEventListener("mouseover", function () {
        t.classList.add("active");
      });

      t.addEventListener("mouseleave", function () {
        t.classList.remove("active");
      });
    }
  }),
  $(document).ready(function () {
    $(".form_group_reg").click(function () {
      $("#authModal").removeClass("active"),
        $("#authModalreg").addClass("active");
    });
  }),
  $(document).ready(function () {
    $(".span_prev").click(function () {
      $("#authModalreg").removeClass("active"),
        $("#authModal").addClass("active");
    });
  }),
  document.addEventListener("DOMContentLoaded", function () {
    let e = document.getElementById("regForm");
    e &&
      e.addEventListener("submit", function (t) {
        t.preventDefault();
        let r = new XMLHttpRequest(),
          a = new FormData(e),
          o = e.getAttribute("method"),
          s = e.getAttribute("action");
        r.open(o, s, !0),
          r.setRequestHeader("X-CSRFToken", a.get("csrfmiddlewaretoken")),
          (r.onload = function () {
            if (200 === r.status) {
              let t = JSON.parse(r.responseText);
              if (t.success)
                t.activation_required
                  ? (document
                      .querySelector("#authModalreg")
                      .classList.remove("active"),
                    document
                      .querySelector("#write_reg")
                      .classList.add("active"))
                  : (document
                      .querySelector("#authModalreg")
                      .classList.remove("active"),
                    window.location.reload());
              else {
                let a = e.querySelector(".error_modal");
                (a.innerHTML = t.message), (a.style.display = "block");
              }
            } else {
              let o = e.querySelector(".error_modal");
              (o.textContent = "Ошибка на сервере. Статус код: " + r.status),
                (o.style.display = "block");
            }
          }),
          r.send(a);
      });
  });
const csrfToken = document.querySelector(
    'input[name="csrfmiddlewaretoken"]'
  ).value,
  logoutForms = document.querySelectorAll(".logout-form");
logoutForms.forEach((e) => {
  e.addEventListener("submit", function (t) {
    t.preventDefault();
    let r = new XMLHttpRequest();
    r.open("POST", e.action),
      r.setRequestHeader("X-CSRFToken", csrfToken),
      (r.onreadystatechange = function () {
        if (r.readyState === XMLHttpRequest.DONE && 200 === r.status) {
          let e = JSON.parse(r.responseText);
          e.success && (window.location.href = "/");
        }
      }),
      r.send();
  });
}),
  document.querySelector("#authForm").addEventListener("submit", function (e) {
    e.preventDefault();
    let t = e.target,
      r = new FormData(t),
      a = new XMLHttpRequest();
    a.open("POST", t.action),
      a.setRequestHeader("X-CSRFToken", r.get("csrfmiddlewaretoken")),
      (a.onreadystatechange = function () {
        if (a.readyState === XMLHttpRequest.DONE) {
          if (200 === a.status) {
            let e = JSON.parse(a.responseText);
            if (e.success)
              document.querySelector(".modal_reg").classList.remove("active"),
                window.location.reload();
            else {
              let r = t.querySelector(".error_modal");
              (r.textContent = e.message), (r.style.display = "block");
            }
          } else {
            let o = t.querySelector(".error_modal");
            (o.textContent = "Ошибка на сервере"), (o.style.display = "block");
          }
        }
      }),
      a.send(r);
  });

const basketForms = document.querySelectorAll(".basket-form"),
  numBasketProductsElements = document.querySelectorAll(".basket_products_num");

let num_basket_products = parseInt(numBasketProductsElements[0].textContent);
let currentButton = null; // Переменная для хранения кнопки, вызвавшей модал

basketForms.forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    const button = form.querySelector(".add-to-basket-btn"),
      productButton = form.querySelector(".basket_prod"),
      actionUrl = form.getAttribute("action"),
      formData = new FormData(form),
      buttonText = productButton.querySelector("p");

    // Сохраняем текущую кнопку, вызвавшую модальное окно, если её ещё нет
    if (!currentButton) {
      currentButton = document.querySelector(
        `.basket_color_btn[data-product-id="${button.getAttribute("data-id")}"]`
      );
    }

    fetch(actionUrl, {
      method: "POST",
      body: formData,
      headers: { "X-CSRFToken": "{{ csrf_token }}" },
    })
      .then((response) => response.json())
      .then((data) => {
        // console.log(data);

        // Проверяем состояние корзины и обновляем классы
        if (data.added) {
          productButton.classList.add("active");
          buttonText && (buttonText.textContent = "Удалить");

          // Обновляем кнопку, вызвавшую модал
          if (currentButton) {
            currentButton.classList.add("active");
          }

          num_basket_products += 1;
        } else {
          productButton.classList.remove("active");
          buttonText && (buttonText.textContent = "В корзину");

          // Убираем класс "active" с кнопки, вызвавшей модал
          if (currentButton) {
            currentButton.classList.remove("active");
          }

          num_basket_products -= 1;
        }

        // Обновляем отображение количества товаров в корзине
        numBasketProductsElements.forEach((el) => {
          el.textContent = num_basket_products;
        });
      })
      .catch((error) => {
        console.error("Ошибка при обработке формы корзины:", error);
      });
  });
});

// Обработчик для открытия модального окна и сохранения текущей кнопки
document.querySelectorAll(".basket_color_btn").forEach((button) => {
  button.addEventListener("click", () => {
    currentButton = button; // Сохраняем кнопку, которая открыла модал
  });
});

$(document).ready(function () {
  $(".dropdown_item_count").click(function (e) {
    e.preventDefault();
    var t = $(this).data("value");
    $("#show_count").text(t),
      $("#show_count_input").val(t),
      $(this).removeAttr("data-value"),
      $(".form_sort_show").submit();
  });
}),
  $(document).ready(function () {
    $(".dropdown_sort").click(function (e) {
      e.preventDefault();
      var t = $(this).data("value");
      $("#show_sort").text($(this).text()),
        $("#show_sort_input").val(t),
        $(this).removeAttr("data-value"),
        $(".form_sort_price").submit();
    });
  }),
  $(document).ready(function () {
    $("#catalog_mobile_btn").click(function (e) {
      e.stopPropagation(), $(".catalog_mobile_main").toggleClass("active");
    }),
      $(document).click(function (e) {
        $(".catalog_mobile_main").is(e.target) ||
          0 !== $(".catalog_mobile_main").has(e.target).length ||
          $(".catalog_mobile_main").removeClass("active");
      });
  }),
  $(document).ready(function () {
    $(".catalog_mobile_item").click(function () {
      $(this).toggleClass("active");
    });
  }),
  $(document).ready(function () {
    let timeout;

    $(".active_catalog").hover(function () {
      clearTimeout(timeout);
      $(".main_menu_header_top").removeClass("active");
      $(this).closest(".main_menu_header_top").addClass("active");
    });
    $(".main_menu_header_top")
      .mouseleave(function () {
        // Устанавливаем таймер для удаления класса "active" через 500 мс
        timeout = setTimeout(() => {
          $(this).removeClass("active");
        }, 500);
      })
      .mouseenter(function () {
        clearTimeout(timeout);
      });
  });

// Выпадающее меню

$(document).ready(function () {
  let timer;

  $("#header_catalog").hover(
    function () {
      clearTimeout(timer);
      $("#down_main_menu").addClass("active");
    },
    function () {
      timer = setTimeout(function () {
        if (!$("#down_main_menu:hover").length) {
          $("#down_main_menu").removeClass("active");
        }
      }, 500); // задержка перед скрытием меню
    }
  );

  $("#down_main_menu").hover(
    function () {
      clearTimeout(timer);
    },
    function () {
      timer = setTimeout(function () {
        $("#down_main_menu").removeClass("active");
      }, 500); // задержка перед скрытием меню
    }
  );
});

$(document).ready(function () {
  $("#header_catalog_top").click(function (event) {
    event.stopPropagation();
    $("#down_main_top").toggleClass("active_top");
  });

  $(document).click(function (event) {
    if (
      !$(event.target).closest("#down_main_top").length &&
      !$(event.target).is("#header_catalog_top")
    ) {
      $("#down_main_top").removeClass("active_top");
    }
  });
});
$(document).ready(function () {
  $(".gallery").magnificPopup({
    delegate: "a", // элемент для открытия попапа
    type: "image",
    gallery: {
      enabled: true, // Галерея
    },
    zoom: {
      enabled: true, // Зум при открытии
      duration: 300, // Длительность анимации
    },
  });
});

$(".delivery_item").click(function () {
  const target = $(this).data("target");

  // Сбрасываем активные классы
  $(".delivery_item").removeClass("active");
  $(".delivery_none").removeClass("active");

  // Добавляем активный класс к текущему элементу и его целевому элементу
  $(this).addClass("active");
  $(target).addClass("active");

  // Установка значения для pickup
  if ($(target).is("#div2")) {
    // Если выбрана доставка
    $("#pickup").val("false"); // Устанавливаем значение в false для pickup
  } else {
    // Если выбран самовывоз
    $("#pickup").val("true"); // Устанавливаем значение в true для pickup
  }
});

$("#uploadForm").submit(function (event) {
  event.preventDefault(); // Останавливаем стандартное действие формы

  var formData = new FormData(this); // Собираем данные формы

  $.ajax({
    url: $(this).attr("action"),
    type: $(this).attr("method"),
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      // Выводим всплывающее сообщение об успехе
      alert(
        "Файл успешно загружен!\nДобавлено: " +
          response.added +
          "\nОбновлено: " +
          response.updated
      );
    },
    error: function (xhr, status, error) {
      alert("Ошибка при загрузке файла: " + xhr.responseText);
    },
  });
});
$(document).ready(function () {
  $(".search_btn").click(function () {
    $(".search_top_main").toggleClass("active");
  });

  $(".escape_search").click(function () {
    $(".search_top_main").removeClass("active");
  });

  $(document).keydown(function (e) {
    if (e.key === "Escape") {
      // Проверяем, нажата ли клавиша Esc
      if ($(".search_top_main").hasClass("active")) {
        $(".search_top_main").removeClass("active");
      }
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("basketModal");
  const buttons = document.querySelectorAll(".basket_color_btn");
  const hiddenSize = document.querySelector(".hiddenSize");

  let currentProductId; // Переменная для хранения текущего productId

  // При нажатии на кнопку открываем модальное окно
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      modal.classList.add("active"); // Добавляем класс для отображения модального окна
      currentProductId = this.getAttribute("data-product-id"); // Получаем productId

      hiddenSize.value = currentProductId;
      // console.log(`Открытие модального окна для productId: ${currentProductId}`);

      // Сначала загружаем данные для модального окна
      fetchDataForModal(currentProductId);
    });
  });

  // При нажатии вне модального окна, закрываем его
  window.onclick = function (event) {
    if (event.target === modal) {
      modal.classList.remove("active");
    }
  };

  function fetchDataForModal(productId) {
    // console.log(`Запрос на получение данных для продукта: ${productId}`);
    return fetch(`/fetch-product-data/${productId}/`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Сеть вернула ошибку");
        }
        return response.json();
      })
      .then((data) => {
        // console.log("Полученные данные продукта:", data);
        const colorSelect = document.querySelector(".color_select");
        const sizeSelect = document.querySelector(".size-select");
        const modalTitle = document.getElementById("modal_title");
        const hiddenColor = document.querySelector(".hiddenColor");
        const hiddenSize = document.querySelector(".hiddenSize");
        const addToBasketButton = document.querySelector(".add-to-basket-btn");

        // console.log("Значение hiddenSize:", hiddenSize.value);

        // Обновляем заголовок модала
        if (modalTitle) {
          modalTitle.textContent = data.title;
        }

        // Обновляем действие формы
        const basketForm = document.getElementById("basket-form-modal");
        if (basketForm) {
          basketForm.action = `/add-to-basket/${productId}/`;
        }

        // Устанавливаем data-id для кнопки
        if (addToBasketButton) {
          addToBasketButton.setAttribute("data-id", productId); // Устанавливаем data-id
        }

        // Очистка селектора цветов и добавление новых опций
        if (colorSelect) {
          colorSelect.innerHTML = ""; // Очищаем текущие опции
          const selectedColorId = data.selected_color_id; // Идентификатор выбранного цвета

          data.colors.forEach((color) => {
            const option = document.createElement("option");
            option.value = color.id; // Уникальный id для каждого цвета
            option.textContent = color.color__name; // Имя цвета (например, Blue, Green)
            colorSelect.appendChild(option);

            // Если текущий цвет совпадает с выбранным цветом
            if (color.color__id === selectedColorId) {
              colorSelect.value = color.id; // Устанавливаем нужный вариант в селекторе
              hiddenColor.value = color.id; // Обновляем скрытое поле с цветом
              // console.log(`Выбранный цвет: ${color.color__name} (ID: ${color.id})`);
            }
          });

          // Если цвет не был найден в списке, установим первый цвет по умолчанию
          if (!colorSelect.value) {
            colorSelect.value = data.colors[0].id;
            hiddenColor.value = data.colors[0].id;
            // console.log(`Цвет по умолчанию: ${data.colors[0].color__name}`);
          }
        }

        // Проверка корзины для обновления цвета и размера
        fetchBasketDetails(productId).then((basketData) => {
          // console.log('fetchBasketDetails', basketData);

          // Флаг, определяющий, был ли товар найден в корзине
          let isFromBasket = false;
          let basketSizeId = null;
          let basketColorId = null;

          // Если товар есть в корзине, устанавливаем цвет и размер
          if (basketData && basketData.product_id) {
            hiddenColor.value = basketData.product_id; // Устанавливаем скрытый цвет
            colorSelect.value = basketData.product_id; // Устанавливаем цвет в селекторе
            // console.log(`Установленный цвет из корзины: ${basketData.color_id}`);

            hiddenSize.value = basketData.size_id; // Устанавливаем скрытый размер
            sizeSelect.value = basketData.size_id; // Устанавливаем размер в селекторе

            // Устанавливаем флаг, что товар был найден в корзине
            isFromBasket = true;
            basketSizeId = basketData.size_id; // Сохраняем ID размера из корзины
            basketColorId = basketData.color_id; // Сохраняем ID цвета из корзины
          }

          // Обновляем доступные размеры для выбранного цвета
          fetchSizes(
            sizeSelect,
            hiddenSize,
            addToBasketButton,
            isFromBasket,
            basketSizeId
          );

          // Дополнительно проверяем цвет и обновляем селектор цветов
          if (colorSelect && basketColorId) {
            // Перебираем все варианты цветов и устанавливаем правильный
            const options = colorSelect.options;
            for (let i = 0; i < options.length; i++) {
              if (options[i].value === basketColorId.toString()) {
                options[i].selected = true; // Устанавливаем выбранный цвет
                hiddenColor.value = basketColorId; // Обновляем скрытое поле
                // console.log(`Цвет ${basketColorId} выбран в селекторе`);
                break;
              }
            }
          } else {
            // console.log("Цвет не был найден в корзине или селектор не определен");
          }
        });
      })
      .catch((error) =>
        console.error("Ошибка при загрузке данных продукта:", error)
      );
  }

  function fetchBasketDetails(productId) {
    return fetch(`/get-basket-product-details/${productId}/`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Сеть вернула ошибку");
        }
        return response.json();
      })
      .then((data) => {
        // console.log(`Детали корзины для productId ${productId}:`, data);
        return data; // Возвращаем данные о цвете и размере
      })
      .catch((error) => {
        console.error("Ошибка при получении деталей корзины:", error);
        return { color_id: null, size_id: null }; // Возвращаем пустые значения в случае ошибки
      });
  }
});

document.addEventListener("DOMContentLoaded", function () {
  // Получаем все формы
  const forms = document.querySelectorAll(".basket-form");

  forms.forEach((form) => {
    const sizeSelect = form.querySelector(".size-select");
    const colorSelect = form.querySelector(".color_select");
    const hiddenSize = form.querySelector(".hiddenSize");
    const button = form.querySelector(".add-to-basket-btn");

    // Проверяем, существует ли элемент sizeSelect
    if (sizeSelect) {
      sizeSelect.addEventListener("change", function () {
        updateHiddenFieldsTwo(sizeSelect, hiddenSize, button);
      });
    }

    // Проверяем, существует ли элемент colorSelect
    if (colorSelect) {
      colorSelect.addEventListener("change", function () {
        button.setAttribute("data-id", colorSelect.value);
        form.action = `/add-to-basket/${colorSelect.value}/`;
        fetchSizes(sizeSelect, hiddenSize, button); // Загружаем размеры
      });
    }
  });
});

// Универсальная функция для обновления скрытых полей
function updateHiddenFieldsTwo(sizeSelect, hiddenSize, button) {
  hiddenSize.value = sizeSelect.value; // Обновляем скрытое поле размера
  const productId = button.getAttribute("data-id");
  checkProductInBasketTwo(productId, sizeSelect.value, button);
}

// Универсальная функция для получения доступных размеров
window.fetchSizes = function (
  sizeSelect,
  hiddenSize,
  button,
  isFromBasket = false,
  basketSizeId = null
) {
  // console.log("fetchSizes");

  if (!button) {
    console.error("Button is undefined in fetchSizes");
    return;
  }

  const productId = button.getAttribute("data-id");
  const url = `/product_sizes/${productId}/`;

  // console.log(`Запрос на получение доступных размеров для product_id: ${productId}`);
  fetch(`${url}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Сеть вернула ошибку");
      }
      return response.json();
    })
    .then((data) => {
      sizeSelect.innerHTML = ""; // Очищаем текущие варианты

      if (data.sizes.length > 0) {
        data.sizes.forEach((size) => {
          const option = document.createElement("option");
          option.value = size.size__id;
          option.textContent = size.size__value;
          sizeSelect.appendChild(option);
        });

        // Если товар был найден в корзине, устанавливаем его размер
        if (isFromBasket && basketSizeId) {
          hiddenSize.value = basketSizeId; // Устанавливаем размер из корзины
          sizeSelect.value = basketSizeId; // Устанавливаем выбранный размер в селекторе
          // console.log(`Размер из корзины установлен: ${basketSizeId}`);
        } else {
          // Если товара нет в корзине, устанавливаем первый доступный размер
          hiddenSize.value = data.sizes[0].size__id; // Устанавливаем первое доступное значение
          // console.log(`Установлен размер по умолчанию: ${hiddenSize.value}`);
        }
      } else {
        const option = document.createElement("option");
        option.textContent = "Нет доступных размеров";
        option.disabled = true;
        sizeSelect.appendChild(option);
        hiddenSize.value = ""; // Если нет доступных размеров, очищаем скрытое поле
      }

      checkProductInBasketTwo(productId, hiddenSize.value, button);
    })
    .catch((error) => console.error("Ошибка при получении размеров:", error));
};

// Универсальная функция для проверки наличия продукта в корзине
function checkProductInBasketTwo(productId, sizeId, button) {
  // console.log('checkProductInBasketTwo');
  // console.log(`Проверка наличия продукта в корзине для productId: ${productId}, sizeId: ${sizeId}`);

  const checkUrl = `/check-basket/${productId}/`;
  fetch(`${checkUrl}?size_id=${sizeId}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Ошибка сети");
      }
      return response.json();
    })
    .then((data) => {
      console.log('Результат проверки наличия продукта в корзине:', data);

      // Уточняем контейнер кнопки для модального окна
      const buttonContainer = document.querySelector(".button_stock_modal");
      // console.log('buttonContainer2:', buttonContainer);

      if (!buttonContainer) {
        console.error("Не удалось найти контейнер кнопки.");
        return;
      }

      // Проверка наличия товара
      if (data.is_in_stock) {
        // console.log('Товар есть в наличии.');
        const existingSoldOutText = buttonContainer.querySelector(
          ".sold-out-text-modal"
        );
        if (existingSoldOutText) {
          existingSoldOutText.remove(); // Удаляем "Sold Out"
          button.classList.remove("remove", data.exists);

        }

        if (!buttonContainer.contains(button)) {
          buttonContainer.appendChild(button); // Добавляем кнопку
        }

        // Обновляем текст кнопки
        const buttonText = button.querySelector("p");
        // console.log('Обновляем текст кнопки:', buttonText.textContent);
        buttonText.textContent = data.exists ? "Удалить" : "В корзину";

        // Обновляем стиль кнопки
        button.classList.toggle("active", data.exists);
      } else {
        // console.log('Товар нет в наличии.');
        if (buttonContainer.contains(button)) {
          button.classList.add("remove", data.exists);

        }

        const existingSoldOutText = buttonContainer.querySelector(
          ".sold-out-text-modal"
        );
        if (!existingSoldOutText) {
          // console.log('Создаем и добавляем текст "Sold Out"');
          const soldOutText = document.createElement("p");
          soldOutText.textContent = "Sold Out";
          soldOutText.classList.add("sold-out-text-modal");
          buttonContainer.appendChild(soldOutText);
        }
      }
    })
    .catch((error) => {
      console.error("Ошибка при проверке корзины:", error);
    });
}

window.addEventListener("load", function () {
  // Находим элементы
  var itemLeft = document.querySelector(".item_left_width");
  var itemRight = document.querySelector(".item_rigth_width");

  // Проверяем, что оба элемента существуют на странице
  if (itemLeft && itemRight) {
    // Получаем ширину элемента .item_left_width
    var leftWidth = window.getComputedStyle(itemLeft).width;

    // Применяем эту ширину к элементу .item_right_width
    itemRight.style.width = leftWidth;
  }
});
