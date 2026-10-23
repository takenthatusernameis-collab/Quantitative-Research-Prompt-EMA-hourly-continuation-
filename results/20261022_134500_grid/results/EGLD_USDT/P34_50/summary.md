# EMA Hourly Continuation — EGLD/USDT P34_50

**Symbol:** EGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 918 |
| net_profit_factor | 0.3018 |
| net_win_rate | 0.4259 |
| gross_profit_factor | 0.7937 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -9.6533 |
| sortino_ratio | -4.1567 |
| max_drawdown | 0.9951 |
| cagr | -0.8795 |
| net_avg_win | 10.9992 |
| net_avg_loss | -27.0427 |
| avg_hold_time_bars | 2.7582 |
| exposure | 0.1151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
