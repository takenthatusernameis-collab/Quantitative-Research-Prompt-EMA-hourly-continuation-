# EMA Hourly Continuation — ZIL/USDT P8_200

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.7036 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 1.0418 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -2.1511 |
| sortino_ratio | -0.6071 |
| max_drawdown | 0.5561 |
| cagr | -0.2471 |
| net_avg_win | 61.4223 |
| net_avg_loss | -86.8574 |
| avg_hold_time_bars | 43.4835 |
| exposure | 0.7807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
