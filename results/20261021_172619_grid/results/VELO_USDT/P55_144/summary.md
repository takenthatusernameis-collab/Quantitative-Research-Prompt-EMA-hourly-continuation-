# EMA Hourly Continuation — VELO/USDT P55_144

**Symbol:** VELO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.9319 |
| net_win_rate | 0.5293 |
| gross_profit_factor | 1.1097 |
| gross_win_rate | 0.5293 |
| sharpe_ratio | -0.3545 |
| sortino_ratio | -0.0992 |
| max_drawdown | 0.2123 |
| cagr | -0.0495 |
| net_avg_win | 82.3281 |
| net_avg_loss | -99.3270 |
| avg_hold_time_bars | 13.4388 |
| exposure | 0.2297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
