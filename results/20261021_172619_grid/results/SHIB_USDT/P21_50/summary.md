# EMA Hourly Continuation — SHIB/USDT P21_50

**Symbol:** SHIB/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6983 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9879 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -2.4786 |
| sortino_ratio | -0.7318 |
| max_drawdown | 0.6065 |
| cagr | -0.2838 |
| net_avg_win | 63.1471 |
| net_avg_loss | -87.4911 |
| avg_hold_time_bars | 6.4941 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
