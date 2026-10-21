# EMA Hourly Continuation — ROSE/USDT P26_50

**Symbol:** ROSE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.5927 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 1.0174 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -6.8253 |
| sortino_ratio | -3.0956 |
| max_drawdown | 0.9776 |
| cagr | -0.7753 |
| net_avg_win | 29.7889 |
| net_avg_loss | -43.6686 |
| avg_hold_time_bars | 3.6023 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
