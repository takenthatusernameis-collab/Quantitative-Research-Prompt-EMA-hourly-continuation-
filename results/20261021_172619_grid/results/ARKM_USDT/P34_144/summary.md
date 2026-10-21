# EMA Hourly Continuation — ARKM/USDT P34_144

**Symbol:** ARKM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.7931 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9419 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -1.3366 |
| sortino_ratio | -0.3730 |
| max_drawdown | 0.3833 |
| cagr | -0.1590 |
| net_avg_win | 72.2993 |
| net_avg_loss | -87.4190 |
| avg_hold_time_bars | 20.1780 |
| exposure | 0.3504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
