# EMA Hourly Continuation — METIS/USDT P12_26

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.7146 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9836 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -2.7562 |
| sortino_ratio | -0.9125 |
| max_drawdown | 0.6656 |
| cagr | -0.3410 |
| net_avg_win | 62.5137 |
| net_avg_loss | -83.0102 |
| avg_hold_time_bars | 5.5861 |
| exposure | 0.1356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
