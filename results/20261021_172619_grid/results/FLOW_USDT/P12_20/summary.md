# EMA Hourly Continuation — FLOW/USDT P12_20

**Symbol:** FLOW/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.5771 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8677 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -3.2009 |
| sortino_ratio | -0.8820 |
| max_drawdown | 0.6402 |
| cagr | -0.3309 |
| net_avg_win | 50.4251 |
| net_avg_loss | -76.2843 |
| avg_hold_time_bars | 4.5501 |
| exposure | 0.0763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
