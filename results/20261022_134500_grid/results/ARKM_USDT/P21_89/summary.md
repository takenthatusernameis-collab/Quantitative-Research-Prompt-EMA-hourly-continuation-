# EMA Hourly Continuation — ARKM/USDT P21_89

**Symbol:** ARKM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.5895 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -4.5756 |
| sortino_ratio | -1.7855 |
| max_drawdown | 0.8815 |
| cagr | -0.5694 |
| net_avg_win | 36.0849 |
| net_avg_loss | -51.8758 |
| avg_hold_time_bars | 10.2136 |
| exposure | 0.3542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
