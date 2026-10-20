# EMA Hourly Continuation — YFI/USDT P21_100

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 768 |
| net_profit_factor | 0.5023 |
| net_win_rate | 0.4323 |
| gross_profit_factor | 0.9238 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -6.7660 |
| sortino_ratio | -2.6184 |
| max_drawdown | 0.9639 |
| cagr | -0.7291 |
| net_avg_win | 29.2663 |
| net_avg_loss | -44.3704 |
| avg_hold_time_bars | 11.7083 |
| exposure | 0.4069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
