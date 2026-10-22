# EMA Hourly Continuation — PEOPLE/USDT P26_100

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.7633 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9286 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -1.5757 |
| sortino_ratio | -0.4597 |
| max_drawdown | 0.4748 |
| cagr | -0.1911 |
| net_avg_win | 64.8594 |
| net_avg_loss | -81.7953 |
| avg_hold_time_bars | 19.9833 |
| exposure | 0.3798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
