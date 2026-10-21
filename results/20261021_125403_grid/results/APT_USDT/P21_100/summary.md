# EMA Hourly Continuation — APT/USDT P21_100

**Symbol:** APT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.7696 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9488 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.6690 |
| sortino_ratio | -0.4958 |
| max_drawdown | 0.4824 |
| cagr | -0.2048 |
| net_avg_win | 68.9644 |
| net_avg_loss | -85.9559 |
| avg_hold_time_bars | 19.9330 |
| exposure | 0.3923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
