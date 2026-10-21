# EMA Hourly Continuation — NOT/USDT P50_100

**Symbol:** NOT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7469 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9474 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.5753 |
| sortino_ratio | -0.4265 |
| max_drawdown | 0.3903 |
| cagr | -0.1780 |
| net_avg_win | 65.4094 |
| net_avg_loss | -85.5680 |
| avg_hold_time_bars | 8.7572 |
| exposure | 0.1423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
