# EMA Hourly Continuation — CFG/USDT P21_55

**Symbol:** CFG/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.4947 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.8593 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -5.6687 |
| sortino_ratio | -2.1769 |
| max_drawdown | 0.9331 |
| cagr | -0.6492 |
| net_avg_win | 27.4514 |
| net_avg_loss | -44.3624 |
| avg_hold_time_bars | 12.3530 |
| exposure | 0.4183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
