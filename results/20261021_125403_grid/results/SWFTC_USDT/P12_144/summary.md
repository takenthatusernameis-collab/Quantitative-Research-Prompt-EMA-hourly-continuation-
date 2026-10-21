# EMA Hourly Continuation — SWFTC/USDT P12_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7135 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8662 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -2.3257 |
| sortino_ratio | -0.6961 |
| max_drawdown | 0.5655 |
| cagr | -0.2741 |
| net_avg_win | 67.1469 |
| net_avg_loss | -80.3834 |
| avg_hold_time_bars | 27.2067 |
| exposure | 0.5503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
