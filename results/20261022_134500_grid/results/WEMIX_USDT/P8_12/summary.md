# EMA Hourly Continuation — WEMIX/USDT P8_12

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2381 |
| net_profit_factor | 0.0756 |
| net_win_rate | 0.2083 |
| gross_profit_factor | 0.2618 |
| gross_win_rate | 0.2617 |
| sharpe_ratio | -29.1851 |
| sortino_ratio | -21.5867 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 1.6487 |
| net_avg_loss | -5.7389 |
| avg_hold_time_bars | 1.8484 |
| exposure | 0.2000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
