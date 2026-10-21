# EMA Hourly Continuation — ZBCN/USDT P26_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.9615 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.1067 |
| gross_win_rate | 0.5281 |
| sharpe_ratio | -0.2070 |
| sortino_ratio | -0.0609 |
| max_drawdown | 0.3125 |
| cagr | -0.0343 |
| net_avg_win | 95.4680 |
| net_avg_loss | -111.1218 |
| avg_hold_time_bars | 21.2249 |
| exposure | 0.4016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
