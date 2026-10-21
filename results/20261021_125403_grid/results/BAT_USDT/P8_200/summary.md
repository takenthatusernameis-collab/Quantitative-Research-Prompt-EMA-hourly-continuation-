# EMA Hourly Continuation — BAT/USDT P8_200

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.9037 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0896 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -0.4566 |
| sortino_ratio | -0.1101 |
| max_drawdown | 0.1936 |
| cagr | -0.0523 |
| net_avg_win | 80.5562 |
| net_avg_loss | -97.7931 |
| avg_hold_time_bars | 63.4520 |
| exposure | 0.8105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
