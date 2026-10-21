# EMA Hourly Continuation — SEI/USDT P20_100

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.9154 |
| net_win_rate | 0.5259 |
| gross_profit_factor | 1.1032 |
| gross_win_rate | 0.5259 |
| sharpe_ratio | -0.5755 |
| sortino_ratio | -0.1706 |
| max_drawdown | 0.3133 |
| cagr | -0.0799 |
| net_avg_win | 91.5650 |
| net_avg_loss | -110.9700 |
| avg_hold_time_bars | 23.3986 |
| exposure | 0.4510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
