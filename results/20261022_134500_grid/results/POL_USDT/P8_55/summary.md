# EMA Hourly Continuation — POL/USDT P8_55

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1029 |
| net_profit_factor | 0.4447 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.7936 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -7.1071 |
| sortino_ratio | -3.1995 |
| max_drawdown | 0.9807 |
| cagr | -0.7922 |
| net_avg_win | 16.8177 |
| net_avg_loss | -31.4245 |
| avg_hold_time_bars | 11.2089 |
| exposure | 0.5243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
