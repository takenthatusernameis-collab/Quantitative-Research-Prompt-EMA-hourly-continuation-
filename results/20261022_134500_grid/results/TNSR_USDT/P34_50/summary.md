# EMA Hourly Continuation — TNSR/USDT P34_50

**Symbol:** TNSR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 892 |
| net_profit_factor | 0.5278 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.9388 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -7.3302 |
| sortino_ratio | -3.0692 |
| max_drawdown | 0.9794 |
| cagr | -0.7831 |
| net_avg_win | 27.0131 |
| net_avg_loss | -42.5637 |
| avg_hold_time_bars | 3.1581 |
| exposure | 0.1275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
