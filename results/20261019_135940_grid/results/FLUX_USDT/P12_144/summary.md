# EMA Hourly Continuation — FLUX/USDT P12_144

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.7061 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -2.2602 |
| sortino_ratio | -0.7163 |
| max_drawdown | 0.5829 |
| cagr | -0.2857 |
| net_avg_win | 55.7151 |
| net_avg_loss | -76.4152 |
| avg_hold_time_bars | 29.4360 |
| exposure | 0.6690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
