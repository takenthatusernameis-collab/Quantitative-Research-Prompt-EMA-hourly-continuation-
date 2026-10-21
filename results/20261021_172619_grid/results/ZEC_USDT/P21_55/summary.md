# EMA Hourly Continuation — ZEC/USDT P21_55

**Symbol:** ZEC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.8971 |
| net_win_rate | 0.5304 |
| gross_profit_factor | 1.1304 |
| gross_win_rate | 0.5304 |
| sharpe_ratio | -0.6993 |
| sortino_ratio | -0.2088 |
| max_drawdown | 0.2879 |
| cagr | -0.0952 |
| net_avg_win | 85.3296 |
| net_avg_loss | -107.4228 |
| avg_hold_time_bars | 8.7126 |
| exposure | 0.1695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
