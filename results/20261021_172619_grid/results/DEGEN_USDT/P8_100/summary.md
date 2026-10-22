# EMA Hourly Continuation — DEGEN/USDT P8_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.9283 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0682 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -0.4940 |
| sortino_ratio | -0.1462 |
| max_drawdown | 0.2932 |
| cagr | -0.0703 |
| net_avg_win | 98.8041 |
| net_avg_loss | -113.7016 |
| avg_hold_time_bars | 35.9434 |
| exposure | 0.6939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
