# EMA Hourly Continuation — CELR/USDT P8_26

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.6773 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9351 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -3.8670 |
| sortino_ratio | -1.6027 |
| max_drawdown | 0.8451 |
| cagr | -0.5195 |
| net_avg_win | 43.9887 |
| net_avg_loss | -59.0702 |
| avg_hold_time_bars | 6.4585 |
| exposure | 0.2467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
