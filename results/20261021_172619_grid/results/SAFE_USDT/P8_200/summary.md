# EMA Hourly Continuation — SAFE/USDT P8_200

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.9790 |
| net_win_rate | 0.5359 |
| gross_profit_factor | 1.1410 |
| gross_win_rate | 0.5359 |
| sharpe_ratio | -0.0733 |
| sortino_ratio | -0.0194 |
| max_drawdown | 0.1647 |
| cagr | -0.0151 |
| net_avg_win | 96.8288 |
| net_avg_loss | -114.2219 |
| avg_hold_time_bars | 50.2784 |
| exposure | 0.7691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
