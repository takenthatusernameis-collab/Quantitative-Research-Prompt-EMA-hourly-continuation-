# EMA Hourly Continuation — HTX/USDT P8_20

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1777 |
| net_profit_factor | 0.1108 |
| net_win_rate | 0.2296 |
| gross_profit_factor | 0.4279 |
| gross_win_rate | 0.3196 |
| sharpe_ratio | -24.3119 |
| sortino_ratio | -15.8975 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 3.0526 |
| net_avg_loss | -8.2144 |
| avg_hold_time_bars | 3.2943 |
| exposure | 0.2649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
