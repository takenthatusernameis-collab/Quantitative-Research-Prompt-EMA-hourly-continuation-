# EMA Hourly Continuation — CATI/USDT P12_55

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 870 |
| net_profit_factor | 0.4991 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.7715 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -7.6123 |
| sortino_ratio | -3.4699 |
| max_drawdown | 0.9718 |
| cagr | -0.8139 |
| net_avg_win | 26.2643 |
| net_avg_loss | -38.5733 |
| avg_hold_time_bars | 8.6632 |
| exposure | 0.4131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
