# EMA Hourly Continuation — GMT/USDT P8_21

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1707 |
| net_profit_factor | 0.2747 |
| net_win_rate | 0.4247 |
| gross_profit_factor | 0.7028 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -12.8072 |
| sortino_ratio | -7.4788 |
| max_drawdown | 0.9999 |
| cagr | -0.9781 |
| net_avg_win | 5.2242 |
| net_avg_loss | -14.0396 |
| avg_hold_time_bars | 2.9549 |
| exposure | 0.2293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
