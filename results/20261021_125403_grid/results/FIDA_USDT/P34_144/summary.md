# EMA Hourly Continuation — FIDA/USDT P34_144

**Symbol:** FIDA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7293 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9311 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -2.0335 |
| sortino_ratio | -0.5848 |
| max_drawdown | 0.5071 |
| cagr | -0.2363 |
| net_avg_win | 67.4898 |
| net_avg_loss | -85.9870 |
| avg_hold_time_bars | 21.2885 |
| exposure | 0.3940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
