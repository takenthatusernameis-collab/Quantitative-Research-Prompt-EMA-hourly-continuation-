# EMA Hourly Continuation — ORCA/USDT P50_89

**Symbol:** ORCA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.5043 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8950 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -5.0623 |
| sortino_ratio | -1.7387 |
| max_drawdown | 0.8885 |
| cagr | -0.5729 |
| net_avg_win | 32.2772 |
| net_avg_loss | -55.6003 |
| avg_hold_time_bars | 6.0067 |
| exposure | 0.1633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
