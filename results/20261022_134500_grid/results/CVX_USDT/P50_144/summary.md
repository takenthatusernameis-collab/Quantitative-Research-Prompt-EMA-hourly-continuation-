# EMA Hourly Continuation — CVX/USDT P50_144

**Symbol:** CVX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.5327 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.7862 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -4.0614 |
| sortino_ratio | -1.2518 |
| max_drawdown | 0.7798 |
| cagr | -0.4526 |
| net_avg_win | 41.7289 |
| net_avg_loss | -61.8014 |
| avg_hold_time_bars | 12.2733 |
| exposure | 0.2695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
