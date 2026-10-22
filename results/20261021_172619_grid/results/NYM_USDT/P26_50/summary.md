# EMA Hourly Continuation — NYM/USDT P26_50

**Symbol:** NYM/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.4351 |
| net_win_rate | 0.4294 |
| gross_profit_factor | 0.7586 |
| gross_win_rate | 0.4294 |
| sharpe_ratio | -4.4422 |
| sortino_ratio | -1.1698 |
| max_drawdown | 0.7481 |
| cagr | -0.4215 |
| net_avg_win | 39.4119 |
| net_avg_loss | -68.1685 |
| avg_hold_time_bars | 11.2265 |
| exposure | 0.1735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
