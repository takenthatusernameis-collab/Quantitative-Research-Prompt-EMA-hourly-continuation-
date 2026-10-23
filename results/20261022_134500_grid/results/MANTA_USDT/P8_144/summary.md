# EMA Hourly Continuation — MANTA/USDT P8_144

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6783 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.9315 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -2.3847 |
| sortino_ratio | -0.6660 |
| max_drawdown | 0.5441 |
| cagr | -0.2669 |
| net_avg_win | 62.7297 |
| net_avg_loss | -81.3139 |
| avg_hold_time_bars | 45.6941 |
| exposure | 0.8080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
