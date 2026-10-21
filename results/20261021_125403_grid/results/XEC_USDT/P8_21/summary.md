# EMA Hourly Continuation — XEC/USDT P8_21

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.5842 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.9119 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -4.7705 |
| sortino_ratio | -1.8730 |
| max_drawdown | 0.8855 |
| cagr | -0.5738 |
| net_avg_win | 34.8722 |
| net_avg_loss | -53.9369 |
| avg_hold_time_bars | 5.7133 |
| exposure | 0.1939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
