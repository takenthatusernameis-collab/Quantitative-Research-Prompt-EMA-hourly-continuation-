# EMA Hourly Continuation — REQ/USDT P144_200

**Symbol:** REQ/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.3300 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.7734 |
| gross_win_rate | 0.3672 |
| sharpe_ratio | -9.8246 |
| sortino_ratio | -3.4111 |
| max_drawdown | 0.9869 |
| cagr | -0.8205 |
| net_avg_win | 25.9918 |
| net_avg_loss | -39.3760 |
| avg_hold_time_bars | 3.7576 |
| exposure | 0.0958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
