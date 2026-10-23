# EMA Hourly Continuation — IOST/USDT P20_50

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 943 |
| net_profit_factor | 0.4294 |
| net_win_rate | 0.4422 |
| gross_profit_factor | 0.8390 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -7.8575 |
| sortino_ratio | -3.3964 |
| max_drawdown | 0.9860 |
| cagr | -0.8157 |
| net_avg_win | 17.7870 |
| net_avg_loss | -32.8406 |
| avg_hold_time_bars | 5.4528 |
| exposure | 0.2337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
