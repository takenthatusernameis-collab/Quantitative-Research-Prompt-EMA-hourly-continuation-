# EMA Hourly Continuation — MOVR/USDT P100_200

**Symbol:** MOVR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.6761 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8576 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -1.9885 |
| sortino_ratio | -0.4836 |
| max_drawdown | 0.4435 |
| cagr | -0.1995 |
| net_avg_win | 65.6942 |
| net_avg_loss | -84.7150 |
| avg_hold_time_bars | 14.3082 |
| exposure | 0.1899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
