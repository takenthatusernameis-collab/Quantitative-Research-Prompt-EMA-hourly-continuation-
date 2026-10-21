# EMA Hourly Continuation — ELON/USDT P8_100

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.7632 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -2.2454 |
| sortino_ratio | -0.7788 |
| max_drawdown | 0.5977 |
| cagr | -0.3010 |
| net_avg_win | 67.3029 |
| net_avg_loss | -81.3157 |
| avg_hold_time_bars | 20.9932 |
| exposure | 0.5649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
