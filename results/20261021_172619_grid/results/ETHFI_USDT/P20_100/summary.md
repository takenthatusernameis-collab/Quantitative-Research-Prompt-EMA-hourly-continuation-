# EMA Hourly Continuation — ETHFI/USDT P20_100

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.8616 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0104 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.0422 |
| sortino_ratio | -0.3134 |
| max_drawdown | 0.3945 |
| cagr | -0.1369 |
| net_avg_win | 87.0546 |
| net_avg_loss | -101.4974 |
| avg_hold_time_bars | 21.6984 |
| exposure | 0.4350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
