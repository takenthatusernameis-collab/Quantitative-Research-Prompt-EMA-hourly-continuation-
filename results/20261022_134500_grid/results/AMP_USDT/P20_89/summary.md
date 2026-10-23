# EMA Hourly Continuation — AMP/USDT P20_89

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1034 |
| net_profit_factor | 0.4180 |
| net_win_rate | 0.3888 |
| gross_profit_factor | 0.7420 |
| gross_win_rate | 0.4014 |
| sharpe_ratio | -9.6526 |
| sortino_ratio | -4.3732 |
| max_drawdown | 0.9959 |
| cagr | -0.8857 |
| net_avg_win | 17.7898 |
| net_avg_loss | -27.0703 |
| avg_hold_time_bars | 8.6799 |
| exposure | 0.4080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
