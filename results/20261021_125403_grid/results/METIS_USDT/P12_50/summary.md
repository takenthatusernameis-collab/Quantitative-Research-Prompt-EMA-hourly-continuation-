# EMA Hourly Continuation — METIS/USDT P12_50

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.6820 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8698 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -3.2396 |
| sortino_ratio | -1.1717 |
| max_drawdown | 0.7574 |
| cagr | -0.4164 |
| net_avg_win | 53.1855 |
| net_avg_loss | -67.0005 |
| avg_hold_time_bars | 12.2767 |
| exposure | 0.3610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
