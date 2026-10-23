# EMA Hourly Continuation — PUNDIX/USDT P12_89

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.5945 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.9204 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -4.9773 |
| sortino_ratio | -1.9156 |
| max_drawdown | 0.9036 |
| cagr | -0.6009 |
| net_avg_win | 38.7115 |
| net_avg_loss | -54.6921 |
| avg_hold_time_bars | 15.7416 |
| exposure | 0.5345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
