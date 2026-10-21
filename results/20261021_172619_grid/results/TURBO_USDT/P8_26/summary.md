# EMA Hourly Continuation — TURBO/USDT P8_26

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.8337 |
| net_win_rate | 0.5179 |
| gross_profit_factor | 1.0681 |
| gross_win_rate | 0.5179 |
| sharpe_ratio | -1.5192 |
| sortino_ratio | -0.5659 |
| max_drawdown | 0.4689 |
| cagr | -0.2304 |
| net_avg_win | 73.2018 |
| net_avg_loss | -94.3280 |
| avg_hold_time_bars | 6.3405 |
| exposure | 0.1930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
