# EMA Hourly Continuation — IOST/USDT P12_21

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1416 |
| net_profit_factor | 0.2653 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.8555 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -13.4661 |
| sortino_ratio | -7.2810 |
| max_drawdown | 0.9999 |
| cagr | -0.9764 |
| net_avg_win | 6.4140 |
| net_avg_loss | -15.9557 |
| avg_hold_time_bars | 3.1010 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
