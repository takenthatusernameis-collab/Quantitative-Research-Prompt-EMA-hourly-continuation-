# EMA Hourly Continuation — SUN/USDT P50_89

**Symbol:** SUN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.2295 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.6076 |
| gross_win_rate | 0.4006 |
| sharpe_ratio | -10.5225 |
| sortino_ratio | -3.7927 |
| max_drawdown | 0.9945 |
| cagr | -0.8729 |
| net_avg_win | 14.2381 |
| net_avg_loss | -31.0253 |
| avg_hold_time_bars | 5.9519 |
| exposure | 0.1681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
