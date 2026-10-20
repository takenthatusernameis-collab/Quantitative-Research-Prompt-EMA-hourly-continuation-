# EMA Hourly Continuation — WOO/USDT P12_200

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8328 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0784 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -1.0690 |
| sortino_ratio | -0.2793 |
| max_drawdown | 0.3182 |
| cagr | -0.1234 |
| net_avg_win | 81.5148 |
| net_avg_loss | -102.6569 |
| avg_hold_time_bars | 49.9464 |
| exposure | 0.7628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
