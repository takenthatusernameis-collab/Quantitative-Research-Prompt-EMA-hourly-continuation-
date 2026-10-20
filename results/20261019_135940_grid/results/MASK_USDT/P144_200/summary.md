# EMA Hourly Continuation — MASK/USDT P144_200

**Symbol:** MASK/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.4104 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8584 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -5.3260 |
| sortino_ratio | -1.6132 |
| max_drawdown | 0.8611 |
| cagr | -0.5430 |
| net_avg_win | 29.0636 |
| net_avg_loss | -59.0596 |
| avg_hold_time_bars | 4.8653 |
| exposure | 0.1002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
