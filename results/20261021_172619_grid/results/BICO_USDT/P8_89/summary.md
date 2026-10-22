# EMA Hourly Continuation — BICO/USDT P8_89

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.8548 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0237 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.1583 |
| sortino_ratio | -0.3849 |
| max_drawdown | 0.4595 |
| cagr | -0.1656 |
| net_avg_win | 79.0682 |
| net_avg_loss | -94.5867 |
| avg_hold_time_bars | 26.9108 |
| exposure | 0.6581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
