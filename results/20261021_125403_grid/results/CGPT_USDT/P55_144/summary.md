# EMA Hourly Continuation — CGPT/USDT P55_144

**Symbol:** CGPT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7780 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 0.9543 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -1.4612 |
| sortino_ratio | -0.3890 |
| max_drawdown | 0.3900 |
| cagr | -0.1645 |
| net_avg_win | 74.9095 |
| net_avg_loss | -92.4713 |
| avg_hold_time_bars | 14.1988 |
| exposure | 0.2240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
