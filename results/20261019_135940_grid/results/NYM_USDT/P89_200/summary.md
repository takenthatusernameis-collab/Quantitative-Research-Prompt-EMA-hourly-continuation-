# EMA Hourly Continuation — NYM/USDT P89_200

**Symbol:** NYM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.3005 |
| net_win_rate | 0.3674 |
| gross_profit_factor | 0.6288 |
| gross_win_rate | 0.3796 |
| sharpe_ratio | -7.0700 |
| sortino_ratio | -2.0315 |
| max_drawdown | 0.9288 |
| cagr | -0.6508 |
| net_avg_win | 26.4250 |
| net_avg_loss | -51.0705 |
| avg_hold_time_bars | 10.7202 |
| exposure | 0.2003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
