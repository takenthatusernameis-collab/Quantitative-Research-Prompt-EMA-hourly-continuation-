# EMA Hourly Continuation — BDX/USDT P50_100

**Symbol:** BDX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.1841 |
| net_win_rate | 0.2644 |
| gross_profit_factor | 0.4754 |
| gross_win_rate | 0.3354 |
| sharpe_ratio | -17.8241 |
| sortino_ratio | -9.1165 |
| max_drawdown | 1.0000 |
| cagr | -0.9934 |
| net_avg_win | 7.6744 |
| net_avg_loss | -14.9832 |
| avg_hold_time_bars | 3.3076 |
| exposure | 0.1672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
