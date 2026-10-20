# EMA Hourly Continuation — ORBS/USDT P55_144

**Symbol:** ORBS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.5261 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.8916 |
| gross_win_rate | 0.4415 |
| sharpe_ratio | -5.4378 |
| sortino_ratio | -1.7493 |
| max_drawdown | 0.8826 |
| cagr | -0.5723 |
| net_avg_win | 43.8878 |
| net_avg_loss | -62.4230 |
| avg_hold_time_bars | 12.1996 |
| exposure | 0.2889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
