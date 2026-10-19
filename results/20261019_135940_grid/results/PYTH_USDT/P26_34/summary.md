# EMA Hourly Continuation — PYTH/USDT P26_34

**Symbol:** PYTH/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1038 |
| net_profit_factor | 0.3291 |
| net_win_rate | 0.4143 |
| gross_profit_factor | 0.8134 |
| gross_win_rate | 0.4383 |
| sharpe_ratio | -10.6564 |
| sortino_ratio | -4.8950 |
| max_drawdown | 0.9983 |
| cagr | -0.9196 |
| net_avg_win | 11.3873 |
| net_avg_loss | -24.4715 |
| avg_hold_time_bars | 1.9383 |
| exposure | 0.0915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
