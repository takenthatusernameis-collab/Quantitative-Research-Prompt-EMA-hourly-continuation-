# EMA Hourly Continuation — DEGEN/USDT P8_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.9626 |
| net_win_rate | 0.5243 |
| gross_profit_factor | 1.0941 |
| gross_win_rate | 0.5243 |
| sharpe_ratio | -0.1845 |
| sortino_ratio | -0.0467 |
| max_drawdown | 0.2501 |
| cagr | -0.0263 |
| net_avg_win | 102.9484 |
| net_avg_loss | -117.8559 |
| avg_hold_time_bars | 55.5631 |
| exposure | 0.7817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
