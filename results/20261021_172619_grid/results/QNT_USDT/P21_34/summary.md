# EMA Hourly Continuation — QNT/USDT P21_34

**Symbol:** QNT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.6955 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0425 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -1.9723 |
| sortino_ratio | -0.4754 |
| max_drawdown | 0.4206 |
| cagr | -0.1953 |
| net_avg_win | 67.6540 |
| net_avg_loss | -100.0933 |
| avg_hold_time_bars | 5.0893 |
| exposure | 0.0648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
