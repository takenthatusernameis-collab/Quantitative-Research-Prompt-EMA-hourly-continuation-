# EMA Hourly Continuation — WOO/USDT P50_200

**Symbol:** WOO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.6585 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -2.4491 |
| sortino_ratio | -0.6480 |
| max_drawdown | 0.5421 |
| cagr | -0.2655 |
| net_avg_win | 61.8919 |
| net_avg_loss | -84.8902 |
| avg_hold_time_bars | 24.6469 |
| exposure | 0.3966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
