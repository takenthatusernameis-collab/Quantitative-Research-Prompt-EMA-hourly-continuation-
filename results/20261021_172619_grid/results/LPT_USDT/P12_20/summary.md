# EMA Hourly Continuation — LPT/USDT P12_20

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.6512 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9548 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -3.1145 |
| sortino_ratio | -0.9129 |
| max_drawdown | 0.6632 |
| cagr | -0.3425 |
| net_avg_win | 60.1786 |
| net_avg_loss | -86.4198 |
| avg_hold_time_bars | 4.6483 |
| exposure | 0.0883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
