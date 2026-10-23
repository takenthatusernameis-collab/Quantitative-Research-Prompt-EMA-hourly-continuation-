# EMA Hourly Continuation — AXL/USDT P20_200

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.6947 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9354 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.9407 |
| sortino_ratio | -0.9392 |
| max_drawdown | 0.6799 |
| cagr | -0.3610 |
| net_avg_win | 62.6207 |
| net_avg_loss | -80.6310 |
| avg_hold_time_bars | 25.1228 |
| exposure | 0.5923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
