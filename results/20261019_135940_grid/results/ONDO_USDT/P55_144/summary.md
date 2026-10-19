# EMA Hourly Continuation — ONDO/USDT P55_144

**Symbol:** ONDO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.5168 |
| net_win_rate | 0.4329 |
| gross_profit_factor | 0.7635 |
| gross_win_rate | 0.4429 |
| sharpe_ratio | -4.3955 |
| sortino_ratio | -1.3910 |
| max_drawdown | 0.8079 |
| cagr | -0.4780 |
| net_avg_win | 39.8384 |
| net_avg_loss | -58.8362 |
| avg_hold_time_bars | 10.3267 |
| exposure | 0.2342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
