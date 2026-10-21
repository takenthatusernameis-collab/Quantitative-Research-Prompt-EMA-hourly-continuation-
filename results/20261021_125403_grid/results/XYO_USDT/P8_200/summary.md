# EMA Hourly Continuation — XYO/USDT P8_200

**Symbol:** XYO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.6035 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.7676 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -3.2832 |
| sortino_ratio | -0.9372 |
| max_drawdown | 0.6842 |
| cagr | -0.3516 |
| net_avg_win | 56.8442 |
| net_avg_loss | -72.2652 |
| avg_hold_time_bars | 39.2268 |
| exposure | 0.7278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
