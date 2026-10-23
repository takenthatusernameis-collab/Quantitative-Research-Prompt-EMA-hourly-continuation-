# EMA Hourly Continuation — LSK/USDT P12_200

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7645 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0460 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -1.6588 |
| sortino_ratio | -0.4569 |
| max_drawdown | 0.5203 |
| cagr | -0.1932 |
| net_avg_win | 70.8444 |
| net_avg_loss | -96.1885 |
| avg_hold_time_bars | 42.9147 |
| exposure | 0.7315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
