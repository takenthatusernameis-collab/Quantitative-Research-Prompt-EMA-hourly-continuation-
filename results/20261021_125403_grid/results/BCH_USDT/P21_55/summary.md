# EMA Hourly Continuation — BCH/USDT P21_55

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6070 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8766 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -3.3945 |
| sortino_ratio | -1.0383 |
| max_drawdown | 0.6984 |
| cagr | -0.3779 |
| net_avg_win | 50.5053 |
| net_avg_loss | -72.6287 |
| avg_hold_time_bars | 9.7330 |
| exposure | 0.2022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
