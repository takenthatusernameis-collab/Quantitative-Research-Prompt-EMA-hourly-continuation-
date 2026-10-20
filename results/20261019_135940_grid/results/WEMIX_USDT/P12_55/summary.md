# EMA Hourly Continuation — WEMIX/USDT P12_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1474 |
| net_profit_factor | 0.2357 |
| net_win_rate | 0.3060 |
| gross_profit_factor | 0.4500 |
| gross_win_rate | 0.3216 |
| sharpe_ratio | -15.9737 |
| sortino_ratio | -8.7818 |
| max_drawdown | 1.0000 |
| cagr | -0.9885 |
| net_avg_win | 6.8363 |
| net_avg_loss | -12.7889 |
| avg_hold_time_bars | 6.2354 |
| exposure | 0.4178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
