# EMA Hourly Continuation — SUSHI/USDT P20_100

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7774 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9660 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.7984 |
| sortino_ratio | -0.5630 |
| max_drawdown | 0.5001 |
| cagr | -0.2289 |
| net_avg_win | 71.1779 |
| net_avg_loss | -87.8375 |
| avg_hold_time_bars | 18.9647 |
| exposure | 0.4136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
