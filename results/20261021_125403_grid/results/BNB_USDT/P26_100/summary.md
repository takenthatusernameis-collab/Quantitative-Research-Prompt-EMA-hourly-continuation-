# EMA Hourly Continuation — BNB/USDT P26_100

**Symbol:** BNB/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6603 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0917 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -2.8103 |
| sortino_ratio | -0.8647 |
| max_drawdown | 0.6459 |
| cagr | -0.3257 |
| net_avg_win | 51.7610 |
| net_avg_loss | -84.0865 |
| avg_hold_time_bars | 15.2873 |
| exposure | 0.3169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
