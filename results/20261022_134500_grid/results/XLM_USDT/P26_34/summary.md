# EMA Hourly Continuation — XLM/USDT P26_34

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1106 |
| net_profit_factor | 0.1239 |
| net_win_rate | 0.3427 |
| gross_profit_factor | 0.7005 |
| gross_win_rate | 0.4213 |
| sharpe_ratio | -14.7651 |
| sortino_ratio | -7.2432 |
| max_drawdown | 0.9999 |
| cagr | -0.9799 |
| net_avg_win | 3.7306 |
| net_avg_loss | -15.6993 |
| avg_hold_time_bars | 2.0063 |
| exposure | 0.1009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
