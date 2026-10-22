# EMA Hourly Continuation — NYM/USDT P100_200

**Symbol:** NYM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.4251 |
| net_win_rate | 0.3877 |
| gross_profit_factor | 0.6358 |
| gross_win_rate | 0.3877 |
| sharpe_ratio | -3.8845 |
| sortino_ratio | -0.8317 |
| max_drawdown | 0.6292 |
| cagr | -0.3244 |
| net_avg_win | 52.6371 |
| net_avg_loss | -78.3991 |
| avg_hold_time_bars | 16.6211 |
| exposure | 0.1715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
