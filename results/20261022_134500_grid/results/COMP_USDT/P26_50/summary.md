# EMA Hourly Continuation — COMP/USDT P26_50

**Symbol:** COMP/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1042 |
| net_profit_factor | 0.3595 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.7855 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -8.6758 |
| sortino_ratio | -3.9770 |
| max_drawdown | 0.9930 |
| cagr | -0.8598 |
| net_avg_win | 12.0085 |
| net_avg_loss | -26.8165 |
| avg_hold_time_bars | 4.1132 |
| exposure | 0.1948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
