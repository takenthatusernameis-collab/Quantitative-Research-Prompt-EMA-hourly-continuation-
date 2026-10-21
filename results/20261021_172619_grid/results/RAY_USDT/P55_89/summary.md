# EMA Hourly Continuation — RAY/USDT P55_89

**Symbol:** RAY/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.9266 |
| net_win_rate | 0.5541 |
| gross_profit_factor | 1.2279 |
| gross_win_rate | 0.5541 |
| sharpe_ratio | -0.3754 |
| sortino_ratio | -0.0938 |
| max_drawdown | 0.2530 |
| cagr | -0.0455 |
| net_avg_win | 84.9955 |
| net_avg_loss | -113.9626 |
| avg_hold_time_bars | 6.9831 |
| exposure | 0.0940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
