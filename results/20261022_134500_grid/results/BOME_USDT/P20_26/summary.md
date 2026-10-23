# EMA Hourly Continuation — BOME/USDT P20_26

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1182 |
| net_profit_factor | 0.3146 |
| net_win_rate | 0.4002 |
| gross_profit_factor | 0.7688 |
| gross_win_rate | 0.4289 |
| sharpe_ratio | -11.6963 |
| sortino_ratio | -5.7370 |
| max_drawdown | 0.9994 |
| cagr | -0.9465 |
| net_avg_win | 9.6986 |
| net_avg_loss | -20.5656 |
| avg_hold_time_bars | 1.8883 |
| exposure | 0.1015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
