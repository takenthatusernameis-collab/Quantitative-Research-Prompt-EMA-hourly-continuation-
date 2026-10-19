# EMA Hourly Continuation — BAT/USDT P20_100

**Symbol:** BAT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.6247 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9970 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -3.6576 |
| sortino_ratio | -1.3346 |
| max_drawdown | 0.8133 |
| cagr | -0.4705 |
| net_avg_win | 40.9772 |
| net_avg_loss | -61.2432 |
| avg_hold_time_bars | 14.0194 |
| exposure | 0.4276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
