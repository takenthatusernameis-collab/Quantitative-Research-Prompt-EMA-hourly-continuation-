# EMA Hourly Continuation — QI/USDT P8_144

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9300 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -3.3444 |
| sortino_ratio | -1.0100 |
| max_drawdown | 0.7370 |
| cagr | -0.3879 |
| net_avg_win | 57.5419 |
| net_avg_loss | -77.1180 |
| avg_hold_time_bars | 33.9002 |
| exposure | 0.7225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
