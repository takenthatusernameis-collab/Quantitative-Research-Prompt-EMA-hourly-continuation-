# EMA Hourly Continuation — COTI/USDT P26_89

**Symbol:** COTI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7949 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 0.9863 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -1.6413 |
| sortino_ratio | -0.5312 |
| max_drawdown | 0.4904 |
| cagr | -0.2177 |
| net_avg_win | 70.1922 |
| net_avg_loss | -87.2774 |
| avg_hold_time_bars | 11.5127 |
| exposure | 0.2674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
