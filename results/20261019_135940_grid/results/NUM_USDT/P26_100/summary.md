# EMA Hourly Continuation — NUM/USDT P26_100

**Symbol:** NUM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.4847 |
| net_win_rate | 0.3826 |
| gross_profit_factor | 0.7220 |
| gross_win_rate | 0.3855 |
| sharpe_ratio | -6.7965 |
| sortino_ratio | -2.5092 |
| max_drawdown | 0.9542 |
| cagr | -0.6992 |
| net_avg_win | 33.8791 |
| net_avg_loss | -43.3206 |
| avg_hold_time_bars | 11.3435 |
| exposure | 0.3558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
