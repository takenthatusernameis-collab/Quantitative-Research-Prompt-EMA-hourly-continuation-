# EMA Hourly Continuation — NYM/USDT P12_55

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.5438 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8198 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -3.8444 |
| sortino_ratio | -1.1900 |
| max_drawdown | 0.7598 |
| cagr | -0.4230 |
| net_avg_win | 41.5064 |
| net_avg_loss | -63.6088 |
| avg_hold_time_bars | 19.4736 |
| exposure | 0.4187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
