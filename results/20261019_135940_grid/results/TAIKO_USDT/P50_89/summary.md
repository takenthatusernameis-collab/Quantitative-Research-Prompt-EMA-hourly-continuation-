# EMA Hourly Continuation — TAIKO/USDT P50_89

**Symbol:** TAIKO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.4256 |
| net_win_rate | 0.4221 |
| gross_profit_factor | 0.7259 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -6.4106 |
| sortino_ratio | -2.2356 |
| max_drawdown | 0.9291 |
| cagr | -0.6669 |
| net_avg_win | 28.1344 |
| net_avg_loss | -48.2964 |
| avg_hold_time_bars | 5.4118 |
| exposure | 0.1503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
