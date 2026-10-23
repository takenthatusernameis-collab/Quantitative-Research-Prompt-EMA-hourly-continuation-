# EMA Hourly Continuation — AURORA/USDT P20_21

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.1011 |
| net_win_rate | 0.2301 |
| gross_profit_factor | 0.4366 |
| gross_win_rate | 0.3282 |
| sharpe_ratio | -18.6001 |
| sortino_ratio | -9.4958 |
| max_drawdown | 1.0000 |
| cagr | -0.9951 |
| net_avg_win | 4.7476 |
| net_avg_loss | -14.0292 |
| avg_hold_time_bars | 2.4301 |
| exposure | 0.1138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
