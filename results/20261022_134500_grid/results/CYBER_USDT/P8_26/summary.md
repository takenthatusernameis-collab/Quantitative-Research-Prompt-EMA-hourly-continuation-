# EMA Hourly Continuation — CYBER/USDT P8_26

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1509 |
| net_profit_factor | 0.4669 |
| net_win_rate | 0.4407 |
| gross_profit_factor | 0.8458 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -9.9944 |
| sortino_ratio | -5.4577 |
| max_drawdown | 0.9989 |
| cagr | -0.9340 |
| net_avg_win | 13.1586 |
| net_avg_loss | -22.2033 |
| avg_hold_time_bars | 4.2982 |
| exposure | 0.2948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
