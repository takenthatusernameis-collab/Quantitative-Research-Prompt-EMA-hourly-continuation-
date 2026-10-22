# EMA Hourly Continuation — MANTA/USDT P50_89

**Symbol:** MANTA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9050 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -2.3962 |
| sortino_ratio | -0.6520 |
| max_drawdown | 0.5406 |
| cagr | -0.2587 |
| net_avg_win | 65.6674 |
| net_avg_loss | -86.8005 |
| avg_hold_time_bars | 8.3113 |
| exposure | 0.1371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
