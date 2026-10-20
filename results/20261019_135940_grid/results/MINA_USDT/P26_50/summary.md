# EMA Hourly Continuation — MINA/USDT P26_50

**Symbol:** MINA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.5656 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 1.0760 |
| gross_win_rate | 0.5005 |
| sharpe_ratio | -6.4003 |
| sortino_ratio | -2.8237 |
| max_drawdown | 0.9708 |
| cagr | -0.7448 |
| net_avg_win | 27.3323 |
| net_avg_loss | -43.6786 |
| avg_hold_time_bars | 4.2884 |
| exposure | 0.1893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
