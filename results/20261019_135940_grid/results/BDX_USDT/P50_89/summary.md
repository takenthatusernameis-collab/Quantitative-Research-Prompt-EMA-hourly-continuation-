# EMA Hourly Continuation — BDX/USDT P50_89

**Symbol:** BDX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1135 |
| net_profit_factor | 0.1559 |
| net_win_rate | 0.2493 |
| gross_profit_factor | 0.4613 |
| gross_win_rate | 0.3286 |
| sharpe_ratio | -18.8104 |
| sortino_ratio | -9.8561 |
| max_drawdown | 1.0000 |
| cagr | -0.9959 |
| net_avg_win | 6.5263 |
| net_avg_loss | -13.9048 |
| avg_hold_time_bars | 2.8634 |
| exposure | 0.1477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
