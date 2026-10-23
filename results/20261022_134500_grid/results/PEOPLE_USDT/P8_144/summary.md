# EMA Hourly Continuation — PEOPLE/USDT P8_144

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7344 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9582 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -2.0870 |
| sortino_ratio | -0.6191 |
| max_drawdown | 0.5319 |
| cagr | -0.2515 |
| net_avg_win | 67.6241 |
| net_avg_loss | -85.2410 |
| avg_hold_time_bars | 37.9501 |
| exposure | 0.7573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
