# EMA Hourly Continuation — CHZ/USDT P34_144

**Symbol:** CHZ/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6754 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 1.0112 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -2.6014 |
| sortino_ratio | -0.7980 |
| max_drawdown | 0.6229 |
| cagr | -0.3144 |
| net_avg_win | 55.1666 |
| net_avg_loss | -78.9481 |
| avg_hold_time_bars | 19.4404 |
| exposure | 0.4153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
