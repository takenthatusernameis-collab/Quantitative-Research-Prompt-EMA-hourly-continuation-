# EMA Hourly Continuation — SAND/USDT P12_26

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1396 |
| net_profit_factor | 0.3395 |
| net_win_rate | 0.4148 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -11.9483 |
| sortino_ratio | -6.3170 |
| max_drawdown | 0.9997 |
| cagr | -0.9609 |
| net_avg_win | 8.8767 |
| net_avg_loss | -18.5272 |
| avg_hold_time_bars | 2.7407 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
