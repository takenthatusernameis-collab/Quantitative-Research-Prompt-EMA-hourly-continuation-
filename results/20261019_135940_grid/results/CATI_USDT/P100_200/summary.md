# EMA Hourly Continuation — CATI/USDT P100_200

**Symbol:** CATI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.4459 |
| net_win_rate | 0.4036 |
| gross_profit_factor | 0.7413 |
| gross_win_rate | 0.4271 |
| sharpe_ratio | -5.6027 |
| sortino_ratio | -1.6859 |
| max_drawdown | 0.8257 |
| cagr | -0.5658 |
| net_avg_win | 42.7825 |
| net_avg_loss | -64.9397 |
| avg_hold_time_bars | 7.8906 |
| exposure | 0.1661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
