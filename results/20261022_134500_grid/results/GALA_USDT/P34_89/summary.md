# EMA Hourly Continuation — GALA/USDT P34_89

**Symbol:** GALA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5709 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -4.8783 |
| sortino_ratio | -1.7946 |
| max_drawdown | 0.8908 |
| cagr | -0.5786 |
| net_avg_win | 37.5378 |
| net_avg_loss | -55.9499 |
| avg_hold_time_bars | 7.9209 |
| exposure | 0.2459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
