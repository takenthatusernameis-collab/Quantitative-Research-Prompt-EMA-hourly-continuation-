# EMA Hourly Continuation — SSV/USDT P12_34

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1362 |
| net_profit_factor | 0.5184 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.8715 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -8.9779 |
| sortino_ratio | -4.6486 |
| max_drawdown | 0.9968 |
| cagr | -0.8979 |
| net_avg_win | 18.1896 |
| net_avg_loss | -26.8138 |
| avg_hold_time_bars | 4.2239 |
| exposure | 0.2603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
