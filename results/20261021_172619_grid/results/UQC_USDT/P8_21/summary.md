# EMA Hourly Continuation — UQC/USDT P8_21

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.3683 |
| net_win_rate | 0.2449 |
| gross_profit_factor | 0.6404 |
| gross_win_rate | 0.3056 |
| sharpe_ratio | -10.4495 |
| sortino_ratio | -3.2778 |
| max_drawdown | 0.9893 |
| cagr | -0.8328 |
| net_avg_win | 52.8905 |
| net_avg_loss | -46.5926 |
| avg_hold_time_bars | 17.2360 |
| exposure | 0.3471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
