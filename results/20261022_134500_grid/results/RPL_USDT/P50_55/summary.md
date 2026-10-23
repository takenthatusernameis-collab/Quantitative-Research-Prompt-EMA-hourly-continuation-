# EMA Hourly Continuation — RPL/USDT P50_55

**Symbol:** RPL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.2786 |
| net_win_rate | 0.3953 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -9.8151 |
| sortino_ratio | -3.9025 |
| max_drawdown | 0.9938 |
| cagr | -0.8660 |
| net_avg_win | 12.5442 |
| net_avg_loss | -29.4354 |
| avg_hold_time_bars | 2.9845 |
| exposure | 0.1045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
