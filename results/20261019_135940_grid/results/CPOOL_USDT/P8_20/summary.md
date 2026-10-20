# EMA Hourly Continuation — CPOOL/USDT P8_20

**Symbol:** CPOOL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1595 |
| net_profit_factor | 0.5538 |
| net_win_rate | 0.4313 |
| gross_profit_factor | 0.8926 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -10.3195 |
| sortino_ratio | -5.7737 |
| max_drawdown | 0.9993 |
| cagr | -0.9441 |
| net_avg_win | 18.0299 |
| net_avg_loss | -24.6939 |
| avg_hold_time_bars | 3.0476 |
| exposure | 0.2210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
