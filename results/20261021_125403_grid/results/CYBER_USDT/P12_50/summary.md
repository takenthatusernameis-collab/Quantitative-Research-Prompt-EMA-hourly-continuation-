# EMA Hourly Continuation — CYBER/USDT P12_50

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.7481 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9716 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.5828 |
| sortino_ratio | -0.9663 |
| max_drawdown | 0.6766 |
| cagr | -0.3582 |
| net_avg_win | 59.3662 |
| net_avg_loss | -76.6202 |
| avg_hold_time_bars | 11.1506 |
| exposure | 0.3467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
