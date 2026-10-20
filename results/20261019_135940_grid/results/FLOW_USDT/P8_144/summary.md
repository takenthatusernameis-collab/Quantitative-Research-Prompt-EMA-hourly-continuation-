# EMA Hourly Continuation — FLOW/USDT P8_144

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.6445 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -2.8906 |
| sortino_ratio | -0.8471 |
| max_drawdown | 0.6575 |
| cagr | -0.3322 |
| net_avg_win | 55.5294 |
| net_avg_loss | -79.6532 |
| avg_hold_time_bars | 39.1109 |
| exposure | 0.7698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
