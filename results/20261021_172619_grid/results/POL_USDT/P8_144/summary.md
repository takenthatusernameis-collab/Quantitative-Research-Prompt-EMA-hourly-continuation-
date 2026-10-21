# EMA Hourly Continuation — POL/USDT P8_144

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.9144 |
| net_win_rate | 0.5275 |
| gross_profit_factor | 1.1011 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -0.4390 |
| sortino_ratio | -0.1110 |
| max_drawdown | 0.2284 |
| cagr | -0.0534 |
| net_avg_win | 84.3540 |
| net_avg_loss | -102.9910 |
| avg_hold_time_bars | 55.1230 |
| exposure | 0.7742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
