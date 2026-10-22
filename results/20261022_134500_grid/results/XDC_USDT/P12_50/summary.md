# EMA Hourly Continuation — XDC/USDT P12_50

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1182 |
| net_profit_factor | 0.2497 |
| net_win_rate | 0.4069 |
| gross_profit_factor | 0.6605 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -11.2114 |
| sortino_ratio | -5.4454 |
| max_drawdown | 0.9992 |
| cagr | -0.9405 |
| net_avg_win | 6.9129 |
| net_avg_loss | -18.9968 |
| avg_hold_time_bars | 5.8638 |
| exposure | 0.3150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
