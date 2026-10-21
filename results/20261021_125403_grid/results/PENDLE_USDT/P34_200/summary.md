# EMA Hourly Continuation — PENDLE/USDT P34_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.7654 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.8885 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -1.3387 |
| sortino_ratio | -0.3146 |
| max_drawdown | 0.3459 |
| cagr | -0.1355 |
| net_avg_win | 77.4676 |
| net_avg_loss | -90.6635 |
| avg_hold_time_bars | 44.4908 |
| exposure | 0.5521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
