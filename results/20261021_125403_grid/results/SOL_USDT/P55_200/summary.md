# EMA Hourly Continuation — SOL/USDT P55_200

**Symbol:** SOL/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.7395 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9362 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -1.3756 |
| sortino_ratio | -0.2979 |
| max_drawdown | 0.3234 |
| cagr | -0.1279 |
| net_avg_win | 73.7341 |
| net_avg_loss | -94.6388 |
| avg_hold_time_bars | 38.9522 |
| exposure | 0.4072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
