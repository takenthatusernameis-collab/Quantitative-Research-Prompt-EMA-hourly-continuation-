# EMA Hourly Continuation — POL/USDT P26_89

**Symbol:** POL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7471 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 0.9873 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.7798 |
| sortino_ratio | -0.5333 |
| max_drawdown | 0.5030 |
| cagr | -0.2174 |
| net_avg_win | 62.0143 |
| net_avg_loss | -83.3819 |
| avg_hold_time_bars | 16.8284 |
| exposure | 0.3343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
