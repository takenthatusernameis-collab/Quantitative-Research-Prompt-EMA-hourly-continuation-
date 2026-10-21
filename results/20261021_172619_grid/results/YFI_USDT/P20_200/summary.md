# EMA Hourly Continuation — YFI/USDT P20_200

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.7821 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -1.3481 |
| sortino_ratio | -0.3529 |
| max_drawdown | 0.3953 |
| cagr | -0.1509 |
| net_avg_win | 70.9395 |
| net_avg_loss | -94.0062 |
| avg_hold_time_bars | 42.5804 |
| exposure | 0.6474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
