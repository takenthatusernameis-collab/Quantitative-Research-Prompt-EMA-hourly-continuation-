# EMA Hourly Continuation — QI/USDT P55_144

**Symbol:** QI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.4717 |
| net_win_rate | 0.4325 |
| gross_profit_factor | 0.7876 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -4.7814 |
| sortino_ratio | -1.5024 |
| max_drawdown | 0.8438 |
| cagr | -0.5170 |
| net_avg_win | 34.4301 |
| net_avg_loss | -55.6327 |
| avg_hold_time_bars | 10.4782 |
| exposure | 0.2390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
