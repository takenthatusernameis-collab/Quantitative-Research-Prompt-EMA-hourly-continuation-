# EMA Hourly Continuation — AEVO/USDT P21_89

**Symbol:** AEVO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.8001 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9965 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.7228 |
| sortino_ratio | -0.5672 |
| max_drawdown | 0.5425 |
| cagr | -0.2306 |
| net_avg_win | 73.0900 |
| net_avg_loss | -90.6638 |
| avg_hold_time_bars | 15.3872 |
| exposure | 0.3704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
