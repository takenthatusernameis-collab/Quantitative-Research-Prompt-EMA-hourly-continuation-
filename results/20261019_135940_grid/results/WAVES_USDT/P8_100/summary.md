# EMA Hourly Continuation — WAVES/USDT P8_100

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 864 |
| net_profit_factor | 0.5198 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.8633 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -6.6359 |
| sortino_ratio | -2.7147 |
| max_drawdown | 0.9683 |
| cagr | -0.7442 |
| net_avg_win | 27.7043 |
| net_avg_loss | -41.4537 |
| avg_hold_time_bars | 15.7824 |
| exposure | 0.6198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
