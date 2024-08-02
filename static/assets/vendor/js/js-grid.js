$(function() {
  $("#jsGrid").jsGrid({
      width: "100%",
      height: "400px",

      inserting: false,
      editing: false,
      sorting: true,
      paging: true,

      data: [
          { "ClientName": "Henry Klein", "OrderNo": "02312", "ProductCost": "$14,500", "Project": "Dashboard", "PaymentMode": "Credit card", "StartDate": "04 Dec 2019", "PaymentStatus": "Approved", "Image": "/static/assets/images/faces/face1.jpg" },
          { "ClientName": "Estella Bryan", "OrderNo": "02312", "ProductCost": "$14,500", "Project": "Website", "PaymentMode": "Cash on delivered", "StartDate": "04 Dec 2019", "PaymentStatus": "Pending", "Image": "/static/assets/images/faces/face2.jpg" },
          { "ClientName": "Lucy Abbott", "OrderNo": "02312", "ProductCost": "$14,500", "Project": "App design", "PaymentMode": "Credit card", "StartDate": "04 Dec 2019", "PaymentStatus": "Rejected", "Image": "/static/assets/images/faces/face5.jpg" },
          { "ClientName": "Peter Gill", "OrderNo": "02312", "ProductCost": "$14,500", "Project": "Development", "PaymentMode": "Online Payment", "StartDate": "04 Dec 2019", "PaymentStatus": "Approved", "Image": "/static/assets/images/faces/face3.jpg" },
          { "ClientName": "Sallie Reyes", "OrderNo": "02312", "ProductCost": "$14,500", "Project": "Website", "PaymentMode": "Credit card", "StartDate": "04 Dec 2019", "PaymentStatus": "Approved", "Image": "/static/assets/images/faces/face4.jpg" }
      ],

      fields: [
          { headerTemplate: function() { return "<input type='checkbox' class='form-check-input' />"; },
            itemTemplate: function(_, item) { return "<input type='checkbox' class='form-check-input' />"; }, width: 20 },
          { name: "ClientName", title: "Client Name", type: "text", width: 150,
            itemTemplate: function(value, item) {
                return $("<div>").append(
                    $("<img>").attr("src", item.Image).css({ height: 30, width: 30 }),
                    $("<span>").text(" " + value).addClass("pl-2")
                );
            }
          },
          { name: "OrderNo", title: "Order No", type: "text", width: 50 },
          { name: "ProductCost", title: "Product Cost", type: "text", width: 70 },
          { name: "Project", title: "Project", type: "text", width: 100 },
          { name: "PaymentMode", title: "Payment Mode", type: "text", width: 100 },
          { name: "StartDate", title: "Start Date", type: "text", width: 100 },
          { name: "PaymentStatus", title: "Payment Status", type: "text", width: 100,
            itemTemplate: function(value) {
                let className;
                switch(value) {
                    case "Approved": className = "badge badge-outline-success"; break;
                    case "Pending": className = "badge badge-outline-warning"; break;
                    case "Rejected": className = "badge badge-outline-danger"; break;
                }
                return $("<div>").addClass(className).text(value);
            }
          }
      ]
  });
});