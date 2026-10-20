# EMA Hourly Continuation — AEVO/USDT P12_21

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1435 |
| net_profit_factor | 0.4136 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.8571 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -11.1373 |
| sortino_ratio | -5.9429 |
| max_drawdown | 0.9995 |
| cagr | -0.9498 |
| net_avg_win | 11.4448 |
| net_avg_loss | -20.8116 |
| avg_hold_time_bars | 2.7819 |
| exposure | 0.1806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
