# EMA Hourly Continuation — SSV/USDT P50_144

**Symbol:** SSV/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.5424 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.8231 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -4.7204 |
| sortino_ratio | -1.5746 |
| max_drawdown | 0.8558 |
| cagr | -0.5269 |
| net_avg_win | 40.7187 |
| net_avg_loss | -58.4982 |
| avg_hold_time_bars | 11.4184 |
| exposure | 0.2914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
