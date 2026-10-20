# EMA Hourly Continuation — ONT/USDT P8_55

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1087 |
| net_profit_factor | 0.6031 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.9723 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -6.6607 |
| sortino_ratio | -3.0648 |
| max_drawdown | 0.9791 |
| cagr | -0.7763 |
| net_avg_win | 30.4925 |
| net_avg_loss | -41.0350 |
| avg_hold_time_bars | 9.4351 |
| exposure | 0.4641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
