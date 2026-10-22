# EMA Hourly Continuation — PUNDIX/USDT P50_55

**Symbol:** PUNDIX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.5742 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9735 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -2.6032 |
| sortino_ratio | -0.5695 |
| max_drawdown | 0.4897 |
| cagr | -0.2294 |
| net_avg_win | 57.3178 |
| net_avg_loss | -95.5853 |
| avg_hold_time_bars | 6.1472 |
| exposure | 0.0645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
