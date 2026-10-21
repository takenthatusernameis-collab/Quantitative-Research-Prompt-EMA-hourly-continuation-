# EMA Hourly Continuation — STRK/USDT P12_144

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7068 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.8228 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -2.0997 |
| sortino_ratio | -0.5688 |
| max_drawdown | 0.4950 |
| cagr | -0.2314 |
| net_avg_win | 70.2202 |
| net_avg_loss | -82.0509 |
| avg_hold_time_bars | 39.6131 |
| exposure | 0.6608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
