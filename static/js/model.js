//created by abraham 
function AppViewModel() {
          var self = this;
           self.title=ko.observable("");
           self.description=ko.observable("");
           self.client=ko.observable("");
           self.clientPriority=ko.observable("");
            self.targetDate=ko.observable("");
            self.productArea=ko.observable("");
           self.submit=function() {
            var data=ko.toJSON(this);
            $.post("/requestSubmit", data, function(retData) {
               alert("here >> "+retData);
            });

        }
         };
         // Activates knockout.js
         ko.applyBindings(new AppViewModel());
