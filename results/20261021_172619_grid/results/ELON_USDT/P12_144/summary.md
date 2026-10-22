# EMA Hourly Continuation — ELON/USDT P12_144

**Symbol:** ELON/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7276 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8832 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -2.2454 |
| sortino_ratio | -0.6592 |
| max_drawdown | 0.5492 |
| cagr | -0.2621 |
| net_avg_win | 71.6563 |
| net_avg_loss | -85.5840 |
| avg_hold_time_bars | 31.1098 |
| exposure | 0.6052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
