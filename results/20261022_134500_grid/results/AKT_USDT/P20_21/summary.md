# EMA Hourly Continuation — AKT/USDT P20_21

**Symbol:** AKT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1113 |
| net_profit_factor | 0.2190 |
| net_win_rate | 0.3082 |
| gross_profit_factor | 0.8308 |
| gross_win_rate | 0.3729 |
| sharpe_ratio | -16.5474 |
| sortino_ratio | -8.2939 |
| max_drawdown | 1.0000 |
| cagr | -0.9913 |
| net_avg_win | 8.1757 |
| net_avg_loss | -16.6288 |
| avg_hold_time_bars | 1.6927 |
| exposure | 0.0856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
