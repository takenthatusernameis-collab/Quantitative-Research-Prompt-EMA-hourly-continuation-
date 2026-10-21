# EMA Hourly Continuation — EDU/USDT P21_50

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6501 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.8712 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -3.0372 |
| sortino_ratio | -1.0545 |
| max_drawdown | 0.7203 |
| cagr | -0.3834 |
| net_avg_win | 46.6003 |
| net_avg_loss | -64.3505 |
| avg_hold_time_bars | 6.9747 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
