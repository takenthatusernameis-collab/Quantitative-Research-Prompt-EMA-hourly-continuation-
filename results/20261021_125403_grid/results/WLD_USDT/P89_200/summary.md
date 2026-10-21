# EMA Hourly Continuation — WLD/USDT P89_200

**Symbol:** WLD/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.8707 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0244 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -0.6353 |
| sortino_ratio | -0.1348 |
| max_drawdown | 0.2411 |
| cagr | -0.0620 |
| net_avg_win | 90.1077 |
| net_avg_loss | -106.3640 |
| avg_hold_time_bars | 19.6986 |
| exposure | 0.1961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
