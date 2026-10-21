# EMA Hourly Continuation — SQD/USDT P20_200

**Symbol:** SQD/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.9245 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0567 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -0.4167 |
| sortino_ratio | -0.1151 |
| max_drawdown | 0.2653 |
| cagr | -0.0561 |
| net_avg_win | 87.0610 |
| net_avg_loss | -100.1566 |
| avg_hold_time_bars | 33.8571 |
| exposure | 0.5681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
