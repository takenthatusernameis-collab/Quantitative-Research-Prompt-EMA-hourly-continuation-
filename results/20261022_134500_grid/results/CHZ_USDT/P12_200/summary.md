# EMA Hourly Continuation — CHZ/USDT P12_200

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.7370 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 1.0171 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.7626 |
| sortino_ratio | -0.4691 |
| max_drawdown | 0.4554 |
| cagr | -0.2011 |
| net_avg_win | 67.8688 |
| net_avg_loss | -91.0592 |
| avg_hold_time_bars | 45.8994 |
| exposure | 0.7469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
