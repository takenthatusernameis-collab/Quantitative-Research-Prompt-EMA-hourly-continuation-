# EMA Hourly Continuation — RSR/USDT P55_144

**Symbol:** RSR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8568 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0365 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -0.8195 |
| sortino_ratio | -0.2159 |
| max_drawdown | 0.2326 |
| cagr | -0.0967 |
| net_avg_win | 78.4214 |
| net_avg_loss | -95.9876 |
| avg_hold_time_bars | 15.7768 |
| exposure | 0.2410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
