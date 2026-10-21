# EMA Hourly Continuation — PYTH/USDT P50_89

**Symbol:** PYTH/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.7251 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9291 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -1.6857 |
| sortino_ratio | -0.4341 |
| max_drawdown | 0.4052 |
| cagr | -0.1807 |
| net_avg_win | 65.7671 |
| net_avg_loss | -86.3242 |
| avg_hold_time_bars | 7.5926 |
| exposure | 0.1118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
