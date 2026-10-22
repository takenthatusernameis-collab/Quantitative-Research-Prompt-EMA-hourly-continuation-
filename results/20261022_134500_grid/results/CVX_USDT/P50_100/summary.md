# EMA Hourly Continuation — CVX/USDT P50_100

**Symbol:** CVX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.5858 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9472 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -4.2190 |
| sortino_ratio | -1.4362 |
| max_drawdown | 0.8294 |
| cagr | -0.4995 |
| net_avg_win | 42.2337 |
| net_avg_loss | -64.6040 |
| avg_hold_time_bars | 6.6045 |
| exposure | 0.1753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
