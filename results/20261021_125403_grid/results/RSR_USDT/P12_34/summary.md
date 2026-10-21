# EMA Hourly Continuation — RSR/USDT P12_34

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.7389 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9403 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -2.2880 |
| sortino_ratio | -0.8049 |
| max_drawdown | 0.6383 |
| cagr | -0.3093 |
| net_avg_win | 57.8581 |
| net_avg_loss | -75.0084 |
| avg_hold_time_bars | 7.0033 |
| exposure | 0.1926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
