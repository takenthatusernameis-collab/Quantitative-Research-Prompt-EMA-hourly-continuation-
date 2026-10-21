# EMA Hourly Continuation — HTX/USDT P12_50

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.4737 |
| net_win_rate | 0.4163 |
| gross_profit_factor | 0.7950 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -6.8961 |
| sortino_ratio | -2.4859 |
| max_drawdown | 0.9483 |
| cagr | -0.6910 |
| net_avg_win | 32.7009 |
| net_avg_loss | -49.2294 |
| avg_hold_time_bars | 12.5423 |
| exposure | 0.3559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
