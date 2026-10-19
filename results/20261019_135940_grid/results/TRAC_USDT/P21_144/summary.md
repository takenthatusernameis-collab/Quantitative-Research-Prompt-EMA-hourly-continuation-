# EMA Hourly Continuation — TRAC/USDT P21_144

**Symbol:** TRAC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.6946 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9812 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -2.8301 |
| sortino_ratio | -0.9129 |
| max_drawdown | 0.6773 |
| cagr | -0.3560 |
| net_avg_win | 58.7208 |
| net_avg_loss | -80.2088 |
| avg_hold_time_bars | 20.5714 |
| exposure | 0.4975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
