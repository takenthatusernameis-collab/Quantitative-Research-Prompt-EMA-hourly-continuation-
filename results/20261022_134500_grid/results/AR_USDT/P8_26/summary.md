# EMA Hourly Continuation — AR/USDT P8_26

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1601 |
| net_profit_factor | 0.4824 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8198 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -9.5040 |
| sortino_ratio | -5.3280 |
| max_drawdown | 0.9987 |
| cagr | -0.9284 |
| net_avg_win | 13.0523 |
| net_avg_loss | -21.7264 |
| avg_hold_time_bars | 3.8001 |
| exposure | 0.2765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
