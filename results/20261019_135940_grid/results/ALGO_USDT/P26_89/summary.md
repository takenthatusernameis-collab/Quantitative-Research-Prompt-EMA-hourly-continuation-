# EMA Hourly Continuation — ALGO/USDT P26_89

**Symbol:** ALGO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.6583 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0582 |
| gross_win_rate | 0.5158 |
| sharpe_ratio | -3.4502 |
| sortino_ratio | -1.2853 |
| max_drawdown | 0.8013 |
| cagr | -0.4592 |
| net_avg_win | 43.0502 |
| net_avg_loss | -66.5264 |
| avg_hold_time_bars | 9.3295 |
| exposure | 0.2960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
