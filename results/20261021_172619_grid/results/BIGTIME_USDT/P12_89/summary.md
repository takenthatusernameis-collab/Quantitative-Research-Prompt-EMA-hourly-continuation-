# EMA Hourly Continuation — BIGTIME/USDT P12_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.8676 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0541 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -0.9952 |
| sortino_ratio | -0.3152 |
| max_drawdown | 0.3553 |
| cagr | -0.1383 |
| net_avg_win | 81.7375 |
| net_avg_loss | -99.3515 |
| avg_hold_time_bars | 24.6074 |
| exposure | 0.5445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
