# EMA Hourly Continuation — RLC/USDT P8_21

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1581 |
| net_profit_factor | 0.4602 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.9779 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -10.4827 |
| sortino_ratio | -5.8733 |
| max_drawdown | 0.9994 |
| cagr | -0.9459 |
| net_avg_win | 12.1556 |
| net_avg_loss | -21.0392 |
| avg_hold_time_bars | 3.4807 |
| exposure | 0.2501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
