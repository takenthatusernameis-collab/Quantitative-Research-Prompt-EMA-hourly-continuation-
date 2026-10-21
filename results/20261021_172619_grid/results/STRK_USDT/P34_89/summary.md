# EMA Hourly Continuation — STRK/USDT P34_89

**Symbol:** STRK/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7736 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9690 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.5941 |
| sortino_ratio | -0.4569 |
| max_drawdown | 0.4666 |
| cagr | -0.1898 |
| net_avg_win | 70.8600 |
| net_avg_loss | -89.3375 |
| avg_hold_time_bars | 11.6633 |
| exposure | 0.2126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
