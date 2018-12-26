$(document).ready(function () {
$('.item_add').on('click', function () {
        var target_href = event.target;
//        console.log(target_href);
        if (target_href) {
//        alert('target is:' + target_href.id)
            //window.location.href = "/basket/edit/" + target_href.name + "/" + target_href.value + "/";
            $.ajax({
                url: "/cart/add/" + target_href.id,

                success: function (data) {
//                    alert(data.quantity)
                    $('.simpleCart_total').text('$' + data.price);
                    $('.simpleCart_quantity').text('(' + data.quantity + ')');
//                    console.log('ajax done');
                },
            });

        }
        else {
        alert('not target');
        }
//        event.preventDefault();
    });
});