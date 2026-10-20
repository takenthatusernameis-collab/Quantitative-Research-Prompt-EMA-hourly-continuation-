# EMA Hourly Continuation — ASTR/USDT P34_200

**Symbol:** ASTR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.6579 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -2.4240 |
| sortino_ratio | -0.6073 |
| max_drawdown | 0.5456 |
| cagr | -0.2527 |
| net_avg_win | 66.2685 |
| net_avg_loss | -89.4756 |
| avg_hold_time_bars | 36.6324 |
| exposure | 0.5321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
