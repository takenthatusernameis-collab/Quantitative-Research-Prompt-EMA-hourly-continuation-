# EMA Hourly Continuation — RUNE/USDT P55_144

**Symbol:** RUNE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.6123 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 0.9506 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -2.7007 |
| sortino_ratio | -0.8008 |
| max_drawdown | 0.6378 |
| cagr | -0.3179 |
| net_avg_win | 43.7276 |
| net_avg_loss | -72.7158 |
| avg_hold_time_bars | 13.5747 |
| exposure | 0.2727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
