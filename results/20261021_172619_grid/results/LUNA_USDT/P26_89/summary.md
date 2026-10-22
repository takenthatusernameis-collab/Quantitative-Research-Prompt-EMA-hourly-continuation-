# EMA Hourly Continuation — LUNA/USDT P26_89

**Symbol:** LUNA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.7808 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 1.0022 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.7476 |
| sortino_ratio | -0.5092 |
| max_drawdown | 0.4789 |
| cagr | -0.2089 |
| net_avg_win | 77.2769 |
| net_avg_loss | -97.0809 |
| avg_hold_time_bars | 13.7585 |
| exposure | 0.2589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
