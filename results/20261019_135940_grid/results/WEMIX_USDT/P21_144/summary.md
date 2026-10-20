# EMA Hourly Continuation — WEMIX/USDT P21_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.3462 |
| net_win_rate | 0.3232 |
| gross_profit_factor | 0.5536 |
| gross_win_rate | 0.3348 |
| sharpe_ratio | -9.6474 |
| sortino_ratio | -3.5999 |
| max_drawdown | 0.9898 |
| cagr | -0.8378 |
| net_avg_win | 23.3905 |
| net_avg_loss | -32.2723 |
| avg_hold_time_bars | 19.4993 |
| exposure | 0.6142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
