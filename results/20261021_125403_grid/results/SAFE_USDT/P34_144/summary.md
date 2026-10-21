# EMA Hourly Continuation — SAFE/USDT P34_144

**Symbol:** SAFE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.8491 |
| net_win_rate | 0.5108 |
| gross_profit_factor | 1.0291 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -0.9301 |
| sortino_ratio | -0.2581 |
| max_drawdown | 0.3034 |
| cagr | -0.1146 |
| net_avg_win | 77.5339 |
| net_avg_loss | -95.3257 |
| avg_hold_time_bars | 24.9409 |
| exposure | 0.4249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
