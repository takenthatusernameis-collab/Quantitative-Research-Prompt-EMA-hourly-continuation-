# EMA Hourly Continuation — REQ/USDT P34_100

**Symbol:** REQ/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 767 |
| net_profit_factor | 0.4852 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.9723 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -7.8163 |
| sortino_ratio | -3.0624 |
| max_drawdown | 0.9796 |
| cagr | -0.7847 |
| net_avg_win | 28.5571 |
| net_avg_loss | -42.8210 |
| avg_hold_time_bars | 8.0222 |
| exposure | 0.2797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
