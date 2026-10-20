# EMA Hourly Continuation — ORBS/USDT P144_200

**Symbol:** ORBS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.3564 |
| net_win_rate | 0.3948 |
| gross_profit_factor | 0.7132 |
| gross_win_rate | 0.4043 |
| sharpe_ratio | -6.4363 |
| sortino_ratio | -1.9048 |
| max_drawdown | 0.9035 |
| cagr | -0.6008 |
| net_avg_win | 29.8598 |
| net_avg_loss | -54.6495 |
| avg_hold_time_bars | 5.5839 |
| exposure | 0.1074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
