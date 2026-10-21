# EMA Hourly Continuation — WIN/USDT P50_89

**Symbol:** WIN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -2.4564 |
| sortino_ratio | -0.6040 |
| max_drawdown | 0.5480 |
| cagr | -0.2428 |
| net_avg_win | 59.2308 |
| net_avg_loss | -88.9938 |
| avg_hold_time_bars | 9.4437 |
| exposure | 0.1258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
