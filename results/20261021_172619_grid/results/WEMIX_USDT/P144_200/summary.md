# EMA Hourly Continuation — WEMIX/USDT P144_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.4369 |
| net_win_rate | 0.3672 |
| gross_profit_factor | 0.5985 |
| gross_win_rate | 0.3672 |
| sharpe_ratio | -3.5239 |
| sortino_ratio | -0.6659 |
| max_drawdown | 0.5466 |
| cagr | -0.2665 |
| net_avg_win | 64.5539 |
| net_avg_loss | -85.7554 |
| avg_hold_time_bars | 8.5706 |
| exposure | 0.0690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
