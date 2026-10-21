# EMA Hourly Continuation — WEMIX/USDT P8_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.5438 |
| net_win_rate | 0.3983 |
| gross_profit_factor | 0.6537 |
| gross_win_rate | 0.3983 |
| sharpe_ratio | -3.5160 |
| sortino_ratio | -0.9163 |
| max_drawdown | 0.6636 |
| cagr | -0.3464 |
| net_avg_win | 57.1008 |
| net_avg_loss | -69.4931 |
| avg_hold_time_bars | 49.5029 |
| exposure | 0.7740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
