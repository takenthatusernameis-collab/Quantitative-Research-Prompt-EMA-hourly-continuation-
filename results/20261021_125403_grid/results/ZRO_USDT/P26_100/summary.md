# EMA Hourly Continuation — ZRO/USDT P26_100

**Symbol:** ZRO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.8804 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0422 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -0.7847 |
| sortino_ratio | -0.2345 |
| max_drawdown | 0.2993 |
| cagr | -0.1057 |
| net_avg_win | 81.8897 |
| net_avg_loss | -97.7650 |
| avg_hold_time_bars | 17.7388 |
| exposure | 0.3490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
