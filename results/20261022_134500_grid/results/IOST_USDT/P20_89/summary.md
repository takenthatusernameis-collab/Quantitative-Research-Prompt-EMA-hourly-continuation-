# EMA Hourly Continuation — IOST/USDT P20_89

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.6208 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0648 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -3.9041 |
| sortino_ratio | -1.4633 |
| max_drawdown | 0.8410 |
| cagr | -0.5093 |
| net_avg_win | 37.7660 |
| net_avg_loss | -62.2105 |
| avg_hold_time_bars | 11.4958 |
| exposure | 0.3731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
