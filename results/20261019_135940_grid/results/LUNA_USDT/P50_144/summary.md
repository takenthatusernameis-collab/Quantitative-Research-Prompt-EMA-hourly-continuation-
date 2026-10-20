# EMA Hourly Continuation — LUNA/USDT P50_144

**Symbol:** LUNA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.4814 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.8412 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -5.5297 |
| sortino_ratio | -1.8959 |
| max_drawdown | 0.9025 |
| cagr | -0.5994 |
| net_avg_win | 32.4867 |
| net_avg_loss | -52.0828 |
| avg_hold_time_bars | 9.7678 |
| exposure | 0.2620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
