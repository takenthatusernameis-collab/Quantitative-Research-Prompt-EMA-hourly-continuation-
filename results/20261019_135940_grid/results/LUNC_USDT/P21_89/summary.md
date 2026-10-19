# EMA Hourly Continuation — LUNC/USDT P21_89

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 804 |
| net_profit_factor | 0.4384 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.7755 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -6.4063 |
| sortino_ratio | -2.5579 |
| max_drawdown | 0.9587 |
| cagr | -0.7114 |
| net_avg_win | 20.8432 |
| net_avg_loss | -38.1628 |
| avg_hold_time_bars | 9.2861 |
| exposure | 0.3394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
