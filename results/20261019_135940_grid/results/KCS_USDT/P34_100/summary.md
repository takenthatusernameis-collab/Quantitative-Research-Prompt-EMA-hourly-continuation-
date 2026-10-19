# EMA Hourly Continuation — KCS/USDT P34_100

**Symbol:** KCS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.2477 |
| net_win_rate | 0.3829 |
| gross_profit_factor | 0.7232 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -9.1827 |
| sortino_ratio | -3.3200 |
| max_drawdown | 0.9867 |
| cagr | -0.8189 |
| net_avg_win | 13.4206 |
| net_avg_loss | -33.6175 |
| avg_hold_time_bars | 10.2199 |
| exposure | 0.2936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
