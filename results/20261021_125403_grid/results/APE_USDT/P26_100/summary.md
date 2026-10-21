# EMA Hourly Continuation — APE/USDT P26_100

**Symbol:** APE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6962 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.8727 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -2.2043 |
| sortino_ratio | -0.6457 |
| max_drawdown | 0.5534 |
| cagr | -0.2571 |
| net_avg_win | 60.2477 |
| net_avg_loss | -77.6143 |
| avg_hold_time_bars | 17.8487 |
| exposure | 0.3432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
