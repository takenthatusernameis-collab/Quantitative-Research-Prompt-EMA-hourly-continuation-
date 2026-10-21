# EMA Hourly Continuation — XLM/USDT P21_26

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 140 |
| net_profit_factor | 0.6801 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0633 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -1.4216 |
| sortino_ratio | -0.2432 |
| max_drawdown | 0.2678 |
| cagr | -0.1048 |
| net_avg_win | 71.6486 |
| net_avg_loss | -111.5438 |
| avg_hold_time_bars | 4.5429 |
| exposure | 0.0289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
