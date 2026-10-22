# EMA Hourly Continuation — VR/USDT P55_89

**Symbol:** VR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.5190 |
| net_win_rate | 0.4112 |
| gross_profit_factor | 0.7424 |
| gross_win_rate | 0.4159 |
| sharpe_ratio | -3.1451 |
| sortino_ratio | -0.6521 |
| max_drawdown | 0.5338 |
| cagr | -0.2620 |
| net_avg_win | 65.4536 |
| net_avg_loss | -88.0760 |
| avg_hold_time_bars | 7.9953 |
| exposure | 0.0778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
