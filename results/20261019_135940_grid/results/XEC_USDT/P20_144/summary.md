# EMA Hourly Continuation — XEC/USDT P20_144

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.6282 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -3.7557 |
| sortino_ratio | -1.2173 |
| max_drawdown | 0.7833 |
| cagr | -0.4405 |
| net_avg_win | 53.2355 |
| net_avg_loss | -72.0504 |
| avg_hold_time_bars | 23.0734 |
| exposure | 0.5544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
