# EMA Hourly Continuation — XYO/USDT P50_200

**Symbol:** XYO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.4966 |
| net_win_rate | 0.4238 |
| gross_profit_factor | 0.7435 |
| gross_win_rate | 0.4342 |
| sharpe_ratio | -4.7871 |
| sortino_ratio | -1.4743 |
| max_drawdown | 0.8399 |
| cagr | -0.5046 |
| net_avg_win | 40.3364 |
| net_avg_loss | -59.7391 |
| avg_hold_time_bars | 17.8810 |
| exposure | 0.3876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
