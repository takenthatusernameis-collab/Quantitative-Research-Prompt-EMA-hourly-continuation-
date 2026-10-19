# EMA Hourly Continuation — IOTA/USDT P12_144

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7468 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0623 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.9830 |
| sortino_ratio | -0.6207 |
| max_drawdown | 0.5673 |
| cagr | -0.2580 |
| net_avg_win | 61.7257 |
| net_avg_loss | -86.4244 |
| avg_hold_time_bars | 30.5152 |
| exposure | 0.6838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
