# EMA Hourly Continuation — DUSK/USDT P8_144

**Symbol:** DUSK/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.9191 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0476 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -0.4420 |
| sortino_ratio | -0.1139 |
| max_drawdown | 0.2390 |
| cagr | -0.0549 |
| net_avg_win | 90.9020 |
| net_avg_loss | -103.9474 |
| avg_hold_time_bars | 53.1366 |
| exposure | 0.7777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
