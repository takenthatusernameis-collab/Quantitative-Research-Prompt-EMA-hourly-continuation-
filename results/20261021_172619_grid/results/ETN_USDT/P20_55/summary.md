# EMA Hourly Continuation — ETN/USDT P20_55

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.5487 |
| net_win_rate | 0.4129 |
| gross_profit_factor | 0.7038 |
| gross_win_rate | 0.4129 |
| sharpe_ratio | -4.0642 |
| sortino_ratio | -1.2133 |
| max_drawdown | 0.7036 |
| cagr | -0.4293 |
| net_avg_win | 54.6612 |
| net_avg_loss | -70.0481 |
| avg_hold_time_bars | 10.0643 |
| exposure | 0.2039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
