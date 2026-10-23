# EMA Hourly Continuation — PUNDIX/USDT P8_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.6164 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9413 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -4.2720 |
| sortino_ratio | -1.5976 |
| max_drawdown | 0.8589 |
| cagr | -0.5317 |
| net_avg_win | 41.9594 |
| net_avg_loss | -58.8618 |
| avg_hold_time_bars | 20.2219 |
| exposure | 0.6462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
