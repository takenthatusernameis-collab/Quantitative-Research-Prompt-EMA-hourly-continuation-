# EMA Hourly Continuation — CATI/USDT P50_89

**Symbol:** CATI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.6192 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.8116 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -2.7439 |
| sortino_ratio | -0.6992 |
| max_drawdown | 0.5085 |
| cagr | -0.2754 |
| net_avg_win | 66.2208 |
| net_avg_loss | -87.3015 |
| avg_hold_time_bars | 8.4532 |
| exposure | 0.1237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
