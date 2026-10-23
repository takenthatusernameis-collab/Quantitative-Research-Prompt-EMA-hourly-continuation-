# EMA Hourly Continuation — ORCA/USDT P12_26

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.5452 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 1.0144 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -7.3236 |
| sortino_ratio | -3.6177 |
| max_drawdown | 0.9901 |
| cagr | -0.8316 |
| net_avg_win | 20.1170 |
| net_avg_loss | -33.7498 |
| avg_hold_time_bars | 3.8467 |
| exposure | 0.2156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
