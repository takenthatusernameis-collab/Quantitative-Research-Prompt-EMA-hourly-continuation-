# EMA Hourly Continuation — COMP/USDT P50_144

**Symbol:** COMP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.5870 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9861 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -3.5335 |
| sortino_ratio | -1.1257 |
| max_drawdown | 0.7629 |
| cagr | -0.4220 |
| net_avg_win | 41.6727 |
| net_avg_loss | -69.0927 |
| avg_hold_time_bars | 12.4952 |
| exposure | 0.2936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
