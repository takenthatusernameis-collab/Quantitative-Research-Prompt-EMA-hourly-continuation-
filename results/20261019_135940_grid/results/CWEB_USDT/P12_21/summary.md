# EMA Hourly Continuation — CWEB/USDT P12_21

**Symbol:** CWEB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1396 |
| net_profit_factor | 0.1975 |
| net_win_rate | 0.2228 |
| gross_profit_factor | 0.6244 |
| gross_win_rate | 0.2693 |
| sharpe_ratio | -21.1689 |
| sortino_ratio | -12.1102 |
| max_drawdown | 1.0000 |
| cagr | -0.9989 |
| net_avg_win | 7.9141 |
| net_avg_loss | -11.4850 |
| avg_hold_time_bars | 3.6805 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
