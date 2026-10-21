# EMA Hourly Continuation — ZRX/USDT P144_200

**Symbol:** ZRX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.8287 |
| net_win_rate | 0.5574 |
| gross_profit_factor | 1.2481 |
| gross_win_rate | 0.5574 |
| sharpe_ratio | -0.8821 |
| sortino_ratio | -0.1999 |
| max_drawdown | 0.2600 |
| cagr | -0.0884 |
| net_avg_win | 73.7787 |
| net_avg_loss | -112.1077 |
| avg_hold_time_bars | 5.9836 |
| exposure | 0.0664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
