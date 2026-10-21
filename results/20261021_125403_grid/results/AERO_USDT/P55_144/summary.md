# EMA Hourly Continuation — AERO/USDT P55_144

**Symbol:** AERO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8854 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0707 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.5845 |
| sortino_ratio | -0.1395 |
| max_drawdown | 0.2370 |
| cagr | -0.0645 |
| net_avg_win | 83.2990 |
| net_avg_loss | -101.9222 |
| avg_hold_time_bars | 17.1382 |
| exposure | 0.2142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
