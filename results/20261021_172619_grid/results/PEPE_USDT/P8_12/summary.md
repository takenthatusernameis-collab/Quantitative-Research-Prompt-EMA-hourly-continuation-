# EMA Hourly Continuation — PEPE/USDT P8_12

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 182 |
| net_profit_factor | 0.9004 |
| net_win_rate | 0.5440 |
| gross_profit_factor | 1.1817 |
| gross_win_rate | 0.5440 |
| sharpe_ratio | -0.4082 |
| sortino_ratio | -0.0798 |
| max_drawdown | 0.1401 |
| cagr | -0.0376 |
| net_avg_win | 83.9054 |
| net_avg_loss | -111.1459 |
| avg_hold_time_bars | 4.1374 |
| exposure | 0.0342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
