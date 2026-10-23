# EMA Hourly Continuation — AMP/USDT P50_100

**Symbol:** AMP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 878 |
| net_profit_factor | 0.3397 |
| net_win_rate | 0.3724 |
| gross_profit_factor | 0.6721 |
| gross_win_rate | 0.3986 |
| sharpe_ratio | -9.8629 |
| sortino_ratio | -4.1549 |
| max_drawdown | 0.9949 |
| cagr | -0.8745 |
| net_avg_win | 15.6444 |
| net_avg_loss | -27.3342 |
| avg_hold_time_bars | 5.6002 |
| exposure | 0.2235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
