using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using Web_Client.Models;

namespace Web_Client.Controllers
{
    public class HomeController : Controller
    {

        public IActionResult Index()
        {
            return View();
        }

        public IActionResult LogReg()
        {
            return View();
        }

        public IActionResult TimeSeriesMovingAvg()
        {
            return View();
        }



        [HttpPost]
        public async Task<IActionResult> Model1(float a, float b, float c, float d)
        {
            var httpClient = new HttpClient();

            var URL = $"http://localhost:8070/model1?a={a}&b={b}&c={c}&d={d}";
            var response = await httpClient.GetAsync(URL);
            var result = await response.Content.ReadAsStringAsync();
            var output = new { msg = result };
            TempData["result"] = result;

            return View("LogReg");
        }

        public IActionResult Redirect(int Model)
        {
            if (Model == 1)
            {
                return RedirectToAction("LogReg");
            }
            else
            {
                return RedirectToAction("TimeSeriesMovingAvg");
            }
        }

        [HttpPost]
        public async Task<IActionResult> Model2(string x)
        {
            var httpClient = new HttpClient();
            x = x.Trim();
            var URL = $"http://localhost:8070/model2?x={x}";
            var response = await httpClient.GetAsync(URL);
            var result = await response.Content.ReadAsStringAsync();

            TempData["result"] = result;

            return View("TimeSeriesMovingAvg");
        }
    }
}