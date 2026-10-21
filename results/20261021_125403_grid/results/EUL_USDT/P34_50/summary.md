# EMA Hourly Continuation — EUL/USDT P34_50

**Symbol:** EUL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.5882 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.8247 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -2.4212 |
| sortino_ratio | -0.6044 |
| max_drawdown | 0.5086 |
| cagr | -0.2414 |
| net_avg_win | 49.6276 |
| net_avg_loss | -75.4645 |
| avg_hold_time_bars | 5.7672 |
| exposure | 0.0800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
