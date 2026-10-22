# EMA Hourly Continuation — CSPR/USDT P100_144

**Symbol:** CSPR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.7038 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9271 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -1.5905 |
| sortino_ratio | -0.3428 |
| max_drawdown | 0.3500 |
| cagr | -0.1458 |
| net_avg_win | 70.6257 |
| net_avg_loss | -94.3395 |
| avg_hold_time_bars | 8.2819 |
| exposure | 0.0855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
