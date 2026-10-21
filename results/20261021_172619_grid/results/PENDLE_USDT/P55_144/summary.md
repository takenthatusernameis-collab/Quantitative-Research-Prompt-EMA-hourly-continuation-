# EMA Hourly Continuation — PENDLE/USDT P55_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7899 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9575 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -1.3138 |
| sortino_ratio | -0.3570 |
| max_drawdown | 0.3812 |
| cagr | -0.1528 |
| net_avg_win | 71.9373 |
| net_avg_loss | -88.5821 |
| avg_hold_time_bars | 15.4044 |
| exposure | 0.2528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
