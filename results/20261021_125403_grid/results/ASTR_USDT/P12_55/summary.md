# EMA Hourly Continuation — ASTR/USDT P12_55

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.8087 |
| net_win_rate | 0.5185 |
| gross_profit_factor | 1.1028 |
| gross_win_rate | 0.5185 |
| sharpe_ratio | -2.0130 |
| sortino_ratio | -0.7348 |
| max_drawdown | 0.6096 |
| cagr | -0.2884 |
| net_avg_win | 72.2591 |
| net_avg_loss | -96.2049 |
| avg_hold_time_bars | 13.5631 |
| exposure | 0.3990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
