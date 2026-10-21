# EMA Hourly Continuation — ZRO/USDT P34_50

**Symbol:** ZRO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.8323 |
| net_win_rate | 0.5236 |
| gross_profit_factor | 1.0811 |
| gross_win_rate | 0.5236 |
| sharpe_ratio | -0.8360 |
| sortino_ratio | -0.1909 |
| max_drawdown | 0.2407 |
| cagr | -0.0851 |
| net_avg_win | 76.2515 |
| net_avg_loss | -100.6930 |
| avg_hold_time_bars | 4.9056 |
| exposure | 0.0559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
