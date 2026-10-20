# EMA Hourly Continuation — MAGIC/USDT P26_89

**Symbol:** MAGIC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6708 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9911 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -3.5605 |
| sortino_ratio | -1.2910 |
| max_drawdown | 0.7895 |
| cagr | -0.4567 |
| net_avg_win | 50.0816 |
| net_avg_loss | -70.4583 |
| avg_hold_time_bars | 11.6225 |
| exposure | 0.3471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
