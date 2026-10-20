# EMA Hourly Continuation — AVA/USDT P12_34

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1240 |
| net_profit_factor | 0.3565 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.7311 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -9.7757 |
| sortino_ratio | -4.8320 |
| max_drawdown | 0.9978 |
| cagr | -0.9116 |
| net_avg_win | 10.4277 |
| net_avg_loss | -21.8367 |
| avg_hold_time_bars | 4.0540 |
| exposure | 0.2285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
