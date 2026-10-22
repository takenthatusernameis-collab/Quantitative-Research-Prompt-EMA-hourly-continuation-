# EMA Hourly Continuation — XRP/USDT P100_200

**Symbol:** XRP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.3613 |
| net_win_rate | 0.4233 |
| gross_profit_factor | 0.7321 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -5.8897 |
| sortino_ratio | -1.7361 |
| max_drawdown | 0.8916 |
| cagr | -0.5852 |
| net_avg_win | 27.2200 |
| net_avg_loss | -55.3122 |
| avg_hold_time_bars | 8.0160 |
| exposure | 0.1592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
