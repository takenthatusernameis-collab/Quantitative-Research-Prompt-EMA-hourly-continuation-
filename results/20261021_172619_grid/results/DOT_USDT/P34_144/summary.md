# EMA Hourly Continuation — DOT/USDT P34_144

**Symbol:** DOT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.8499 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0610 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -0.9444 |
| sortino_ratio | -0.2496 |
| max_drawdown | 0.3227 |
| cagr | -0.1100 |
| net_avg_win | 82.5735 |
| net_avg_loss | -103.0776 |
| avg_hold_time_bars | 25.3343 |
| exposure | 0.3892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
