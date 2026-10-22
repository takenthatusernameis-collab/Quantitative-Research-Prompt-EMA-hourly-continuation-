# EMA Hourly Continuation — NOT/USDT P8_21

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.8906 |
| net_win_rate | 0.5379 |
| gross_profit_factor | 1.1534 |
| gross_win_rate | 0.5379 |
| sharpe_ratio | -0.7094 |
| sortino_ratio | -0.2144 |
| max_drawdown | 0.3188 |
| cagr | -0.0972 |
| net_avg_win | 78.9180 |
| net_avg_loss | -103.1548 |
| avg_hold_time_bars | 5.3318 |
| exposure | 0.1057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
