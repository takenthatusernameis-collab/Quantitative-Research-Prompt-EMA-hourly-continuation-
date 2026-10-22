# EMA Hourly Continuation — POL/USDT P100_144

**Symbol:** POL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.3317 |
| net_win_rate | 0.4107 |
| gross_profit_factor | 0.6736 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -6.8831 |
| sortino_ratio | -2.2153 |
| max_drawdown | 0.9438 |
| cagr | -0.6781 |
| net_avg_win | 21.8455 |
| net_avg_loss | -45.9105 |
| avg_hold_time_bars | 4.0000 |
| exposure | 0.0947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
