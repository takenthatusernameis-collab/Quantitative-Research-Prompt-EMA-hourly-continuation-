# EMA Hourly Continuation — VR/USDT P20_55

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6235 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8286 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -3.0175 |
| sortino_ratio | -0.8380 |
| max_drawdown | 0.6295 |
| cagr | -0.3222 |
| net_avg_win | 59.3466 |
| net_avg_loss | -78.8626 |
| avg_hold_time_bars | 12.1719 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
