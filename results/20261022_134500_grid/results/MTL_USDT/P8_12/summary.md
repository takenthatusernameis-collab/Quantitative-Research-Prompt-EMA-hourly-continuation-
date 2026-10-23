# EMA Hourly Continuation — MTL/USDT P8_12

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1668 |
| net_profit_factor | 0.1897 |
| net_win_rate | 0.3453 |
| gross_profit_factor | 0.6482 |
| gross_win_rate | 0.4203 |
| sharpe_ratio | -17.6855 |
| sortino_ratio | -10.4945 |
| max_drawdown | 1.0000 |
| cagr | -0.9962 |
| net_avg_win | 4.0646 |
| net_avg_loss | -11.3015 |
| avg_hold_time_bars | 2.7482 |
| exposure | 0.2074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
