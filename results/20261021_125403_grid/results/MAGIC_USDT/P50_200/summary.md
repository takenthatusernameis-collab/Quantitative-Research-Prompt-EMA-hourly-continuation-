# EMA Hourly Continuation — MAGIC/USDT P50_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.6827 |
| net_win_rate | 0.4579 |
| gross_profit_factor | 0.8428 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -2.0817 |
| sortino_ratio | -0.5092 |
| max_drawdown | 0.4769 |
| cagr | -0.2097 |
| net_avg_win | 70.5821 |
| net_avg_loss | -87.3384 |
| avg_hold_time_bars | 31.8620 |
| exposure | 0.4301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
