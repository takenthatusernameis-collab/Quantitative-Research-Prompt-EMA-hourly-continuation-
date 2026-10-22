# EMA Hourly Continuation — CSPR/USDT P12_26

**Symbol:** CSPR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6199 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.8198 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -3.0229 |
| sortino_ratio | -0.8400 |
| max_drawdown | 0.6210 |
| cagr | -0.3205 |
| net_avg_win | 59.5700 |
| net_avg_loss | -77.0622 |
| avg_hold_time_bars | 6.1126 |
| exposure | 0.1061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
