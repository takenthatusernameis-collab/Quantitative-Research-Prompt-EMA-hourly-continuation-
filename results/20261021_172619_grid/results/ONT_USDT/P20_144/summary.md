# EMA Hourly Continuation — ONT/USDT P20_144

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.7180 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.8777 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -1.9652 |
| sortino_ratio | -0.5636 |
| max_drawdown | 0.5078 |
| cagr | -0.2292 |
| net_avg_win | 63.5212 |
| net_avg_loss | -79.4127 |
| avg_hold_time_bars | 28.5123 |
| exposure | 0.5264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
