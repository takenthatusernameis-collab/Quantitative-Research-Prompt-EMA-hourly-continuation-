# EMA Hourly Continuation — JUP/USDT P21_89

**Symbol:** JUP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.8234 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9918 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.3694 |
| sortino_ratio | -0.4290 |
| max_drawdown | 0.4345 |
| cagr | -0.1806 |
| net_avg_win | 76.8095 |
| net_avg_loss | -92.5067 |
| avg_hold_time_bars | 15.0208 |
| exposure | 0.3277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
