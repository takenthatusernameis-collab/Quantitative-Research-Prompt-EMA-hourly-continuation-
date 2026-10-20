# EMA Hourly Continuation — SYN/USDT P20_55

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 917 |
| net_profit_factor | 0.5660 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8911 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -5.2847 |
| sortino_ratio | -2.2512 |
| max_drawdown | 0.9350 |
| cagr | -0.6622 |
| net_avg_win | 28.4734 |
| net_avg_loss | -44.0315 |
| avg_hold_time_bars | 6.1581 |
| exposure | 0.2567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
