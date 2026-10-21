# EMA Hourly Continuation — XDC/USDT P8_12

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.4242 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.7174 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -3.6144 |
| sortino_ratio | -0.7655 |
| max_drawdown | 0.5921 |
| cagr | -0.2980 |
| net_avg_win | 47.1548 |
| net_avg_loss | -81.8066 |
| avg_hold_time_bars | 5.9724 |
| exposure | 0.0589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
