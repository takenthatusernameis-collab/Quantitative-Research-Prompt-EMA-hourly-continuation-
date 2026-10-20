# EMA Hourly Continuation — AEVO/USDT P26_50

**Symbol:** AEVO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.4786 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8387 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -7.3677 |
| sortino_ratio | -3.2752 |
| max_drawdown | 0.9828 |
| cagr | -0.7943 |
| net_avg_win | 20.6160 |
| net_avg_loss | -34.0398 |
| avg_hold_time_bars | 3.9818 |
| exposure | 0.1784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
