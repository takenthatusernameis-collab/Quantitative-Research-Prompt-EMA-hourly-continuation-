# EMA Hourly Continuation — MTL/USDT P20_50

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 886 |
| net_profit_factor | 0.4755 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4616 |
| sharpe_ratio | -7.6164 |
| sortino_ratio | -3.1930 |
| max_drawdown | 0.9823 |
| cagr | -0.7949 |
| net_avg_win | 23.3548 |
| net_avg_loss | -37.0580 |
| avg_hold_time_bars | 7.2630 |
| exposure | 0.2912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
