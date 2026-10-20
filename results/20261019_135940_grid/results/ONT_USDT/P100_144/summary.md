# EMA Hourly Continuation — ONT/USDT P100_144

**Symbol:** ONT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.4538 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8936 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -5.1700 |
| sortino_ratio | -1.5724 |
| max_drawdown | 0.8658 |
| cagr | -0.5472 |
| net_avg_win | 33.1030 |
| net_avg_loss | -61.8300 |
| avg_hold_time_bars | 4.1353 |
| exposure | 0.0885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
