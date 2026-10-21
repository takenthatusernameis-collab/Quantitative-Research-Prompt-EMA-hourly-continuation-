# EMA Hourly Continuation — IOTA/USDT P100_144

**Symbol:** IOTA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.7052 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9718 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -1.7570 |
| sortino_ratio | -0.3896 |
| max_drawdown | 0.3970 |
| cagr | -0.1632 |
| net_avg_win | 73.7393 |
| net_avg_loss | -100.2830 |
| avg_hold_time_bars | 7.2176 |
| exposure | 0.0784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
