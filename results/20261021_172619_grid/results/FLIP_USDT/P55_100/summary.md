# EMA Hourly Continuation — FLIP/USDT P55_100

**Symbol:** FLIP/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.5823 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8801 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -2.8404 |
| sortino_ratio | -0.6685 |
| max_drawdown | 0.5612 |
| cagr | -0.2690 |
| net_avg_win | 59.7827 |
| net_avg_loss | -88.1048 |
| avg_hold_time_bars | 13.7418 |
| exposure | 0.1718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
