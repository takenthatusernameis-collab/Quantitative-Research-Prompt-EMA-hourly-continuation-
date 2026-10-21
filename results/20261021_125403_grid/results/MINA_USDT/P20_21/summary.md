# EMA Hourly Continuation — MINA/USDT P20_21

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 0.6866 |
| net_win_rate | 0.5122 |
| gross_profit_factor | 1.0465 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -1.6895 |
| sortino_ratio | -0.3473 |
| max_drawdown | 0.4113 |
| cagr | -0.1482 |
| net_avg_win | 69.1833 |
| net_avg_loss | -105.8062 |
| avg_hold_time_bars | 4.8683 |
| exposure | 0.0454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
