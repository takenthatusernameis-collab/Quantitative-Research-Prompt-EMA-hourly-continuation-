# EMA Hourly Continuation — DEXE/USDT P55_144

**Symbol:** DEXE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.8847 |
| net_win_rate | 0.5310 |
| gross_profit_factor | 1.1027 |
| gross_win_rate | 0.5310 |
| sharpe_ratio | -0.5106 |
| sortino_ratio | -0.1181 |
| max_drawdown | 0.2983 |
| cagr | -0.0553 |
| net_avg_win | 74.5610 |
| net_avg_loss | -95.4178 |
| avg_hold_time_bars | 36.0891 |
| exposure | 0.4232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
