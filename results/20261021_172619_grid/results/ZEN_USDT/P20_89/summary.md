# EMA Hourly Continuation — ZEN/USDT P20_89

**Symbol:** ZEN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.7857 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9844 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.7061 |
| sortino_ratio | -0.5494 |
| max_drawdown | 0.4945 |
| cagr | -0.2249 |
| net_avg_win | 68.7721 |
| net_avg_loss | -86.4974 |
| avg_hold_time_bars | 16.1834 |
| exposure | 0.3730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
