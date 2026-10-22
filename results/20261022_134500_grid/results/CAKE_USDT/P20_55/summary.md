# EMA Hourly Continuation — CAKE/USDT P20_55

**Symbol:** CAKE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 865 |
| net_profit_factor | 0.4128 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.8449 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -7.1430 |
| sortino_ratio | -2.9627 |
| max_drawdown | 0.9741 |
| cagr | -0.7653 |
| net_avg_win | 17.8280 |
| net_avg_loss | -34.4771 |
| avg_hold_time_bars | 6.5295 |
| exposure | 0.2567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
