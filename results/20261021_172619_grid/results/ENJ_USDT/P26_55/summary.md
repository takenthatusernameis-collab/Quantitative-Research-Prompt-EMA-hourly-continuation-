# EMA Hourly Continuation — ENJ/USDT P26_55

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.7668 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0522 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -2.0443 |
| sortino_ratio | -0.6435 |
| max_drawdown | 0.5760 |
| cagr | -0.2558 |
| net_avg_win | 70.7856 |
| net_avg_loss | -94.2496 |
| avg_hold_time_bars | 6.5238 |
| exposure | 0.1426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
