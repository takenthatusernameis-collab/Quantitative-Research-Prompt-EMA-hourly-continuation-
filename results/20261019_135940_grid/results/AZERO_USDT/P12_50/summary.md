# EMA Hourly Continuation — AZERO/USDT P12_50

**Symbol:** AZERO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 961 |
| net_profit_factor | 0.5983 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.9942 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -5.4219 |
| sortino_ratio | -2.3399 |
| max_drawdown | 0.9483 |
| cagr | -0.6826 |
| net_avg_win | 31.6230 |
| net_avg_loss | -45.5795 |
| avg_hold_time_bars | 8.0052 |
| exposure | 0.3481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
