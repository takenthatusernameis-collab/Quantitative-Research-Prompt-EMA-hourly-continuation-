# EMA Hourly Continuation — INJ/USDT P26_55

**Symbol:** INJ/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.8591 |
| net_win_rate | 0.5236 |
| gross_profit_factor | 1.1062 |
| gross_win_rate | 0.5236 |
| sharpe_ratio | -1.0145 |
| sortino_ratio | -0.2937 |
| max_drawdown | 0.3722 |
| cagr | -0.1279 |
| net_avg_win | 84.0229 |
| net_avg_loss | -107.4846 |
| avg_hold_time_bars | 7.2556 |
| exposure | 0.1329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
