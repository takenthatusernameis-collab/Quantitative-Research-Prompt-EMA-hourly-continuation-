# EMA Hourly Continuation — LTC/USDT P12_144

**Symbol:** LTC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.4044 |
| net_win_rate | 0.4330 |
| gross_profit_factor | 0.8281 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -5.8627 |
| sortino_ratio | -1.9099 |
| max_drawdown | 0.9183 |
| cagr | -0.6235 |
| net_avg_win | 25.9656 |
| net_avg_loss | -49.0275 |
| avg_hold_time_bars | 25.1757 |
| exposure | 0.6317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
