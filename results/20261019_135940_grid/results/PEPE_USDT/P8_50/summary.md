# EMA Hourly Continuation — PEPE/USDT P8_50

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1186 |
| net_profit_factor | 0.6304 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9468 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -5.9670 |
| sortino_ratio | -2.8746 |
| max_drawdown | 0.9709 |
| cagr | -0.7546 |
| net_avg_win | 29.2965 |
| net_avg_loss | -42.2847 |
| avg_hold_time_bars | 8.1492 |
| exposure | 0.4393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
