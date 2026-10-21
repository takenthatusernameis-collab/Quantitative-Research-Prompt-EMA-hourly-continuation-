# EMA Hourly Continuation — ARKM/USDT P12_55

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.7678 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9359 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.2993 |
| sortino_ratio | -0.8111 |
| max_drawdown | 0.6463 |
| cagr | -0.3116 |
| net_avg_win | 68.6655 |
| net_avg_loss | -82.1442 |
| avg_hold_time_bars | 12.7467 |
| exposure | 0.3546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
