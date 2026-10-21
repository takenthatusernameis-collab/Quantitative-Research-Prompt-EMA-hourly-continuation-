# EMA Hourly Continuation — ZIL/USDT P8_55

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.7891 |
| net_win_rate | 0.5127 |
| gross_profit_factor | 1.0291 |
| gross_win_rate | 0.5127 |
| sharpe_ratio | -1.7418 |
| sortino_ratio | -0.6291 |
| max_drawdown | 0.6085 |
| cagr | -0.2525 |
| net_avg_win | 59.8675 |
| net_avg_loss | -79.8133 |
| avg_hold_time_bars | 16.7927 |
| exposure | 0.4824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
