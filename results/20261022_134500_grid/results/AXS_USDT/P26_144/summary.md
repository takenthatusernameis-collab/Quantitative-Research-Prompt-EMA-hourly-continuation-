# EMA Hourly Continuation — AXS/USDT P26_144

**Symbol:** AXS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.7894 |
| net_win_rate | 0.5277 |
| gross_profit_factor | 1.1523 |
| gross_win_rate | 0.5362 |
| sharpe_ratio | -1.6811 |
| sortino_ratio | -0.5149 |
| max_drawdown | 0.4958 |
| cagr | -0.2184 |
| net_avg_win | 69.9867 |
| net_avg_loss | -99.0377 |
| avg_hold_time_bars | 21.5085 |
| exposure | 0.4574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
