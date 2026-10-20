# EMA Hourly Continuation — NYM/USDT P34_200

**Symbol:** NYM/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.3002 |
| net_win_rate | 0.3505 |
| gross_profit_factor | 0.5552 |
| gross_win_rate | 0.3652 |
| sharpe_ratio | -6.8841 |
| sortino_ratio | -1.9644 |
| max_drawdown | 0.9204 |
| cagr | -0.6343 |
| net_avg_win | 27.5950 |
| net_avg_loss | -49.6104 |
| avg_hold_time_bars | 24.9608 |
| exposure | 0.4629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
