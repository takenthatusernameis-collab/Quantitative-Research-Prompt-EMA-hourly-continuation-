# EMA Hourly Continuation — EUL/USDT P34_200

**Symbol:** EUL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7070 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8477 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -1.8975 |
| sortino_ratio | -0.4903 |
| max_drawdown | 0.4507 |
| cagr | -0.2017 |
| net_avg_win | 68.1363 |
| net_avg_loss | -82.3810 |
| avg_hold_time_bars | 27.2169 |
| exposure | 0.4107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
