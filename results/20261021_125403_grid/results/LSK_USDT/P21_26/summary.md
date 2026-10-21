# EMA Hourly Continuation — LSK/USDT P21_26

**Symbol:** LSK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.5458 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.9486 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -3.8954 |
| sortino_ratio | -1.0884 |
| max_drawdown | 0.7215 |
| cagr | -0.3945 |
| net_avg_win | 49.1792 |
| net_avg_loss | -78.4566 |
| avg_hold_time_bars | 5.0984 |
| exposure | 0.0871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
