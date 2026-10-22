# EMA Hourly Continuation — SUPER/USDT P26_89

**Symbol:** SUPER/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.6624 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -3.1169 |
| sortino_ratio | -1.1503 |
| max_drawdown | 0.7671 |
| cagr | -0.4189 |
| net_avg_win | 42.8127 |
| net_avg_loss | -64.8243 |
| avg_hold_time_bars | 10.7048 |
| exposure | 0.3314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
