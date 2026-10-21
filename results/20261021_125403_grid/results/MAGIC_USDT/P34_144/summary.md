# EMA Hourly Continuation — MAGIC/USDT P34_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.7155 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8926 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -2.0637 |
| sortino_ratio | -0.5509 |
| max_drawdown | 0.4972 |
| cagr | -0.2247 |
| net_avg_win | 71.9635 |
| net_avg_loss | -88.7468 |
| avg_hold_time_bars | 28.0540 |
| exposure | 0.4489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
