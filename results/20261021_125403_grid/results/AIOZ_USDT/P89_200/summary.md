# EMA Hourly Continuation — AIOZ/USDT P89_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.8145 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 1.0020 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -1.1809 |
| sortino_ratio | -0.2874 |
| max_drawdown | 0.3526 |
| cagr | -0.1248 |
| net_avg_win | 86.7467 |
| net_avg_loss | -105.7630 |
| avg_hold_time_bars | 13.2111 |
| exposure | 0.1735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
