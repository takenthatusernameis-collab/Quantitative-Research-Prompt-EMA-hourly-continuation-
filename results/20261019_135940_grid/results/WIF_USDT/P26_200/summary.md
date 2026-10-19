# EMA Hourly Continuation — WIF/USDT P26_200

**Symbol:** WIF/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6218 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8104 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -2.8779 |
| sortino_ratio | -0.8330 |
| max_drawdown | 0.6483 |
| cagr | -0.3255 |
| net_avg_win | 53.4994 |
| net_avg_loss | -72.1998 |
| avg_hold_time_bars | 29.0284 |
| exposure | 0.5581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
