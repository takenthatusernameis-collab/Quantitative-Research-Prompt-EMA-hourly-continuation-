# EMA Hourly Continuation — NEO/USDT P55_144

**Symbol:** NEO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.5030 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8895 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -4.7496 |
| sortino_ratio | -1.5510 |
| max_drawdown | 0.8464 |
| cagr | -0.5222 |
| net_avg_win | 35.1262 |
| net_avg_loss | -58.5196 |
| avg_hold_time_bars | 9.6867 |
| exposure | 0.2347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
