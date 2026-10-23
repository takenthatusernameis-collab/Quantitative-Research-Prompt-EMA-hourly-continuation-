# EMA Hourly Continuation — ALT/USDT P34_200

**Symbol:** ALT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6286 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8349 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -2.9361 |
| sortino_ratio | -0.8148 |
| max_drawdown | 0.6268 |
| cagr | -0.3172 |
| net_avg_win | 60.6580 |
| net_avg_loss | -77.1998 |
| avg_hold_time_bars | 30.4884 |
| exposure | 0.5363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
