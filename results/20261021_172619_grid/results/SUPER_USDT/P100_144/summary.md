# EMA Hourly Continuation — SUPER/USDT P100_144

**Symbol:** SUPER/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.7150 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 0.9699 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.4317 |
| sortino_ratio | -0.3116 |
| max_drawdown | 0.3274 |
| cagr | -0.1335 |
| net_avg_win | 65.3340 |
| net_avg_loss | -92.1763 |
| avg_hold_time_bars | 6.4286 |
| exposure | 0.0675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
