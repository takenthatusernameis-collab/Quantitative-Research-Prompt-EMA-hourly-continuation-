# EMA Hourly Continuation — JASMY/USDT P20_21

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 80 |
| net_profit_factor | 0.6345 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8471 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -1.2283 |
| sortino_ratio | -0.1568 |
| max_drawdown | 0.1739 |
| cagr | -0.0694 |
| net_avg_win | 77.5671 |
| net_avg_loss | -105.1978 |
| avg_hold_time_bars | 4.3750 |
| exposure | 0.0159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
