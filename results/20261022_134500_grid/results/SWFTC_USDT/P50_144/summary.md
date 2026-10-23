# EMA Hourly Continuation — SWFTC/USDT P50_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.4888 |
| net_win_rate | 0.4202 |
| gross_profit_factor | 0.7961 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -5.6782 |
| sortino_ratio | -1.8645 |
| max_drawdown | 0.9023 |
| cagr | -0.6000 |
| net_avg_win | 37.5736 |
| net_avg_loss | -55.7050 |
| avg_hold_time_bars | 9.9853 |
| exposure | 0.2474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
