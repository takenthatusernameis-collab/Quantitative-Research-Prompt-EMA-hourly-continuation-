# EMA Hourly Continuation — ADA/USDT P100_200

**Symbol:** ADA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.7498 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9877 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.3757 |
| sortino_ratio | -0.3050 |
| max_drawdown | 0.3108 |
| cagr | -0.1310 |
| net_avg_win | 74.8399 |
| net_avg_loss | -98.9822 |
| avg_hold_time_bars | 12.9540 |
| exposure | 0.1407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
