# EMA Hourly Continuation — ZETA/USDT P8_89

**Symbol:** ZETA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.9024 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0926 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -0.7181 |
| sortino_ratio | -0.2248 |
| max_drawdown | 0.3540 |
| cagr | -0.1026 |
| net_avg_win | 88.6979 |
| net_avg_loss | -107.8214 |
| avg_hold_time_bars | 30.7542 |
| exposure | 0.6624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
