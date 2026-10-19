# EMA Hourly Continuation — COMP/USDT P12_26

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1460 |
| net_profit_factor | 0.2583 |
| net_win_rate | 0.4096 |
| gross_profit_factor | 0.7052 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -12.4846 |
| sortino_ratio | -6.7819 |
| max_drawdown | 0.9998 |
| cagr | -0.9671 |
| net_avg_win | 5.8233 |
| net_avg_loss | -15.6386 |
| avg_hold_time_bars | 3.2801 |
| exposure | 0.2177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
