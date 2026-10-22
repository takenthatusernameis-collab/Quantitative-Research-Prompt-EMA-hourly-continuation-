# EMA Hourly Continuation — BLUR/USDT P8_100

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.9215 |
| net_win_rate | 0.5317 |
| gross_profit_factor | 1.1241 |
| gross_win_rate | 0.5317 |
| sharpe_ratio | -0.5109 |
| sortino_ratio | -0.1544 |
| max_drawdown | 0.3393 |
| cagr | -0.0739 |
| net_avg_win | 87.9710 |
| net_avg_loss | -108.3753 |
| avg_hold_time_bars | 34.3145 |
| exposure | 0.6863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
