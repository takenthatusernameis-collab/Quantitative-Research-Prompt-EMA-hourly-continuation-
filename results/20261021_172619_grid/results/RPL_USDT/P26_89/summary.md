# EMA Hourly Continuation — RPL/USDT P26_89

**Symbol:** RPL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7306 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.9260 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -2.3431 |
| sortino_ratio | -0.7589 |
| max_drawdown | 0.5957 |
| cagr | -0.2947 |
| net_avg_win | 64.2886 |
| net_avg_loss | -80.1997 |
| avg_hold_time_bars | 14.9633 |
| exposure | 0.3508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
