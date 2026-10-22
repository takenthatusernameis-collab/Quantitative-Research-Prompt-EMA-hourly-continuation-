# EMA Hourly Continuation — HTX/USDT P12_50

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.2729 |
| net_win_rate | 0.3290 |
| gross_profit_factor | 0.7767 |
| gross_win_rate | 0.3908 |
| sharpe_ratio | -15.1460 |
| sortino_ratio | -7.5102 |
| max_drawdown | 1.0000 |
| cagr | -0.9831 |
| net_avg_win | 9.9275 |
| net_avg_loss | -17.8369 |
| avg_hold_time_bars | 7.7772 |
| exposure | 0.4044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
