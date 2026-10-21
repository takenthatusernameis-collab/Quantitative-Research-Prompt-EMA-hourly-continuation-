# EMA Hourly Continuation — INJ/USDT P50_55

**Symbol:** INJ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 101 |
| net_profit_factor | 0.9161 |
| net_win_rate | 0.5545 |
| gross_profit_factor | 1.2332 |
| gross_win_rate | 0.5545 |
| sharpe_ratio | -0.2453 |
| sortino_ratio | -0.0359 |
| max_drawdown | 0.1052 |
| cagr | -0.0173 |
| net_avg_win | 83.3829 |
| net_avg_loss | -113.2679 |
| avg_hold_time_bars | 4.2079 |
| exposure | 0.0193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
