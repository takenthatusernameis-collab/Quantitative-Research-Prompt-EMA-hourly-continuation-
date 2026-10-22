# EMA Hourly Continuation — AXS/USDT P21_89

**Symbol:** AXS/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.6878 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0798 |
| gross_win_rate | 0.5168 |
| sharpe_ratio | -3.1546 |
| sortino_ratio | -1.1355 |
| max_drawdown | 0.7578 |
| cagr | -0.4184 |
| net_avg_win | 49.7543 |
| net_avg_loss | -73.6755 |
| avg_hold_time_bars | 12.5810 |
| exposure | 0.3723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
