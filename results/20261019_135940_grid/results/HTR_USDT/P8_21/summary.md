# EMA Hourly Continuation — HTR/USDT P8_21

**Symbol:** HTR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1492 |
| net_profit_factor | 0.3618 |
| net_win_rate | 0.3626 |
| gross_profit_factor | 0.6647 |
| gross_win_rate | 0.3773 |
| sharpe_ratio | -12.9508 |
| sortino_ratio | -7.0562 |
| max_drawdown | 0.9999 |
| cagr | -0.9715 |
| net_avg_win | 10.4756 |
| net_avg_loss | -16.4732 |
| avg_hold_time_bars | 3.6971 |
| exposure | 0.2507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
