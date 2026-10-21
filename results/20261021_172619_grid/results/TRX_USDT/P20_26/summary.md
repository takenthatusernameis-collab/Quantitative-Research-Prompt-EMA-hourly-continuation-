# EMA Hourly Continuation — TRX/USDT P20_26

**Symbol:** TRX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 127 |
| net_profit_factor | 0.4167 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.1362 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -2.9859 |
| sortino_ratio | -0.4972 |
| max_drawdown | 0.4436 |
| cagr | -0.2065 |
| net_avg_win | 49.1910 |
| net_avg_loss | -119.9108 |
| avg_hold_time_bars | 8.0787 |
| exposure | 0.0466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
