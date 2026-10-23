# EMA Hourly Continuation — CGPT/USDT P50_89

**Symbol:** CGPT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.4877 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8526 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -5.6342 |
| sortino_ratio | -1.9869 |
| max_drawdown | 0.9178 |
| cagr | -0.6290 |
| net_avg_win | 30.4217 |
| net_avg_loss | -51.7402 |
| avg_hold_time_bars | 5.4234 |
| exposure | 0.1560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
