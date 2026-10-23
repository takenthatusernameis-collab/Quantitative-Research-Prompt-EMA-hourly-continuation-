# EMA Hourly Continuation — API3/USDT P20_144

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.6536 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8887 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -3.3127 |
| sortino_ratio | -1.0865 |
| max_drawdown | 0.7523 |
| cagr | -0.3984 |
| net_avg_win | 54.6328 |
| net_avg_loss | -72.0137 |
| avg_hold_time_bars | 22.3773 |
| exposure | 0.5472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
