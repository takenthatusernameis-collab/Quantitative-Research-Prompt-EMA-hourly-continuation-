# EMA Hourly Continuation — ONT/USDT P20_55

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.5593 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.9704 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -6.4048 |
| sortino_ratio | -2.7272 |
| max_drawdown | 0.9690 |
| cagr | -0.7379 |
| net_avg_win | 28.8472 |
| net_avg_loss | -44.1912 |
| avg_hold_time_bars | 5.5147 |
| exposure | 0.2298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
