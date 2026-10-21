# EMA Hourly Continuation — SUI/USDT P12_55

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.8131 |
| net_win_rate | 0.4991 |
| gross_profit_factor | 1.0072 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -1.6674 |
| sortino_ratio | -0.5604 |
| max_drawdown | 0.5220 |
| cagr | -0.2283 |
| net_avg_win | 75.6583 |
| net_avg_loss | -92.7143 |
| avg_hold_time_bars | 13.2178 |
| exposure | 0.3310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
