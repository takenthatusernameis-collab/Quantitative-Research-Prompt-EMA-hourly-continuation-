# EMA Hourly Continuation — RPL/USDT P26_100

**Symbol:** RPL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.6770 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -3.0627 |
| sortino_ratio | -1.0692 |
| max_drawdown | 0.7234 |
| cagr | -0.3945 |
| net_avg_win | 50.4856 |
| net_avg_loss | -71.2282 |
| avg_hold_time_bars | 14.3279 |
| exposure | 0.3955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
