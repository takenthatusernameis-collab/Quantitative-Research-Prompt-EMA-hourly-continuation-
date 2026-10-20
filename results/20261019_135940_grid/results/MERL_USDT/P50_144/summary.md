# EMA Hourly Continuation — MERL/USDT P50_144

**Symbol:** MERL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6112 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.8364 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -3.7685 |
| sortino_ratio | -1.1690 |
| max_drawdown | 0.7780 |
| cagr | -0.4249 |
| net_avg_win | 55.0731 |
| net_avg_loss | -71.4197 |
| avg_hold_time_bars | 12.5186 |
| exposure | 0.2762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
