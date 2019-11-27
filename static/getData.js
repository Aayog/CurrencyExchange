function getDataOnSelect(){
    var from = document.getElementById('fromCurrency').value;
    var to = document.getElementById('toCurrency').value;
    window.location.href = '/response/'+from+'/'+to;
}