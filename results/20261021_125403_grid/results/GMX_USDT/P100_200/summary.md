# EMA Hourly Continuation — GMX/USDT P100_200

**Symbol:** GMX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.6440 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8550 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -2.6382 |
| sortino_ratio | -0.6693 |
| max_drawdown | 0.5537 |
| cagr | -0.2651 |
| net_avg_win | 67.6665 |
| net_avg_loss | -86.9560 |
| avg_hold_time_bars | 11.6258 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
