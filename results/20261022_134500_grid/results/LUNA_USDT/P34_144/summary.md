# EMA Hourly Continuation — LUNA/USDT P34_144

**Symbol:** LUNA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.5238 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.8570 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -5.6894 |
| sortino_ratio | -2.0138 |
| max_drawdown | 0.9176 |
| cagr | -0.6246 |
| net_avg_win | 36.9907 |
| net_avg_loss | -53.0593 |
| avg_hold_time_bars | 12.4353 |
| exposure | 0.3584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
