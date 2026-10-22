# EMA Hourly Continuation — UNI/USDT P12_144

**Symbol:** UNI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6471 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.9509 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -3.3883 |
| sortino_ratio | -1.0645 |
| max_drawdown | 0.7318 |
| cagr | -0.4054 |
| net_avg_win | 55.6918 |
| net_avg_loss | -76.7891 |
| avg_hold_time_bars | 27.7485 |
| exposure | 0.6420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
