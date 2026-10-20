# EMA Hourly Continuation — GTC/USDT P34_200

**Symbol:** GTC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.5422 |
| net_win_rate | 0.4345 |
| gross_profit_factor | 0.7715 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -3.6421 |
| sortino_ratio | -1.0367 |
| max_drawdown | 0.7276 |
| cagr | -0.3884 |
| net_avg_win | 46.9177 |
| net_avg_loss | -66.4792 |
| avg_hold_time_bars | 25.9053 |
| exposure | 0.4851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
