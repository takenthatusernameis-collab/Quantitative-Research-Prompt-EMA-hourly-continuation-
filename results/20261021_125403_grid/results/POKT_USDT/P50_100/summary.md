# EMA Hourly Continuation — POKT/USDT P50_100

**Symbol:** POKT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6776 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8891 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -2.9235 |
| sortino_ratio | -0.8312 |
| max_drawdown | 0.6483 |
| cagr | -0.3186 |
| net_avg_win | 71.6081 |
| net_avg_loss | -87.0246 |
| avg_hold_time_bars | 9.9231 |
| exposure | 0.1810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
