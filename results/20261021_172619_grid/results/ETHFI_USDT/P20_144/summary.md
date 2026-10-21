# EMA Hourly Continuation — ETHFI/USDT P20_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8630 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -1.0359 |
| sortino_ratio | -0.2936 |
| max_drawdown | 0.3994 |
| cagr | -0.1286 |
| net_avg_win | 94.4183 |
| net_avg_loss | -107.7463 |
| avg_hold_time_bars | 31.1985 |
| exposure | 0.5573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
