# EMA Hourly Continuation — FIDA/USDT P55_200

**Symbol:** FIDA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7142 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.8869 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -1.8423 |
| sortino_ratio | -0.4606 |
| max_drawdown | 0.4358 |
| cagr | -0.1914 |
| net_avg_win | 70.9977 |
| net_avg_loss | -88.4987 |
| avg_hold_time_bars | 26.1613 |
| exposure | 0.3670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
