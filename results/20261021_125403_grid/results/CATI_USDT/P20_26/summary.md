# EMA Hourly Continuation — CATI/USDT P20_26

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 155 |
| net_profit_factor | 0.6529 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.8928 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -1.8631 |
| sortino_ratio | -0.3636 |
| max_drawdown | 0.3080 |
| cagr | -0.1553 |
| net_avg_win | 76.3333 |
| net_avg_loss | -104.0840 |
| avg_hold_time_bars | 5.4710 |
| exposure | 0.0465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
