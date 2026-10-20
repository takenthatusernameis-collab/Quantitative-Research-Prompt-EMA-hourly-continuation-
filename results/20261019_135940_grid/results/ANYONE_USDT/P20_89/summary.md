# EMA Hourly Continuation — ANYONE/USDT P20_89

**Symbol:** ANYONE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.5801 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.7508 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -4.9325 |
| sortino_ratio | -1.8765 |
| max_drawdown | 0.8716 |
| cagr | -0.5923 |
| net_avg_win | 42.2307 |
| net_avg_loss | -54.1252 |
| avg_hold_time_bars | 10.4940 |
| exposure | 0.3532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
