# EMA Hourly Continuation — AIOZ/USDT P50_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 108 |
| net_profit_factor | 0.8749 |
| net_win_rate | 0.5278 |
| gross_profit_factor | 1.1190 |
| gross_win_rate | 0.5278 |
| sharpe_ratio | -0.4408 |
| sortino_ratio | -0.0661 |
| max_drawdown | 0.2189 |
| cagr | -0.0306 |
| net_avg_win | 92.2509 |
| net_avg_loss | -117.8467 |
| avg_hold_time_bars | 6.3056 |
| exposure | 0.0310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
