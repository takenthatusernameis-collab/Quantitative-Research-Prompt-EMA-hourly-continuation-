# EMA Hourly Continuation — MTL/USDT P50_55

**Symbol:** MTL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.2190 |
| net_win_rate | 0.3256 |
| gross_profit_factor | 0.7503 |
| gross_win_rate | 0.4096 |
| sharpe_ratio | -12.5393 |
| sortino_ratio | -5.1493 |
| max_drawdown | 0.9991 |
| cagr | -0.9377 |
| net_avg_win | 11.1161 |
| net_avg_loss | -24.5060 |
| avg_hold_time_bars | 3.6059 |
| exposure | 0.1263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
