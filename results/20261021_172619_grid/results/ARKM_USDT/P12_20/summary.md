# EMA Hourly Continuation — ARKM/USDT P12_20

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.5906 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.7937 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -2.7896 |
| sortino_ratio | -0.6692 |
| max_drawdown | 0.5358 |
| cagr | -0.2633 |
| net_avg_win | 61.3517 |
| net_avg_loss | -82.8374 |
| avg_hold_time_bars | 4.6021 |
| exposure | 0.0594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
