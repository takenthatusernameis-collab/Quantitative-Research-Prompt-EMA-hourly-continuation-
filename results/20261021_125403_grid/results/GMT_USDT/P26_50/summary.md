# EMA Hourly Continuation — GMT/USDT P26_50

**Symbol:** GMT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6744 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9312 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -2.5053 |
| sortino_ratio | -0.7257 |
| max_drawdown | 0.5969 |
| cagr | -0.2824 |
| net_avg_win | 59.4473 |
| net_avg_loss | -81.9093 |
| avg_hold_time_bars | 6.3007 |
| exposure | 0.1171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
