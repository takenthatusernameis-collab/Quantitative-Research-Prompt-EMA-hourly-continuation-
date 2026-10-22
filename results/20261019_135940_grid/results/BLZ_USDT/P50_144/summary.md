# EMA Hourly Continuation — BLZ/USDT P50_144

**Symbol:** BLZ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.5816 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.8901 |
| gross_win_rate | 0.4405 |
| sharpe_ratio | -5.0335 |
| sortino_ratio | -1.6752 |
| max_drawdown | 0.8723 |
| cagr | -0.5518 |
| net_avg_win | 49.8606 |
| net_avg_loss | -64.6281 |
| avg_hold_time_bars | 13.5027 |
| exposure | 0.3440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
