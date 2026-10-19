# EMA Hourly Continuation — TRX/USDT P8_20

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1447 |
| net_profit_factor | 0.0985 |
| net_win_rate | 0.2764 |
| gross_profit_factor | 0.8358 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -21.0267 |
| sortino_ratio | -12.7203 |
| max_drawdown | 1.0000 |
| cagr | -0.9992 |
| net_avg_win | 2.7324 |
| net_avg_loss | -10.5950 |
| avg_hold_time_bars | 3.3110 |
| exposure | 0.2178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
