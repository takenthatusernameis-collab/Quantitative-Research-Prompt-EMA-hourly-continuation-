# EMA Hourly Continuation — POL/USDT P20_100

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.8149 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0373 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -1.2403 |
| sortino_ratio | -0.3684 |
| max_drawdown | 0.4304 |
| cagr | -0.1572 |
| net_avg_win | 70.1730 |
| net_avg_loss | -90.2343 |
| avg_hold_time_bars | 23.9720 |
| exposure | 0.4664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
