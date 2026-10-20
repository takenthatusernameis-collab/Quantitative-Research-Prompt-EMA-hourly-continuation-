# EMA Hourly Continuation — FLOW/USDT P8_89

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5944 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9122 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -4.2673 |
| sortino_ratio | -1.5699 |
| max_drawdown | 0.8609 |
| cagr | -0.5278 |
| net_avg_win | 38.8381 |
| net_avg_loss | -57.6007 |
| avg_hold_time_bars | 21.4451 |
| exposure | 0.6658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
