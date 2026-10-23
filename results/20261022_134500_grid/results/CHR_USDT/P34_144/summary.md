# EMA Hourly Continuation — CHR/USDT P34_144

**Symbol:** CHR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.6854 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9383 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -2.6625 |
| sortino_ratio | -0.8342 |
| max_drawdown | 0.6346 |
| cagr | -0.3247 |
| net_avg_win | 57.3114 |
| net_avg_loss | -78.3662 |
| avg_hold_time_bars | 18.9069 |
| exposure | 0.4226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
