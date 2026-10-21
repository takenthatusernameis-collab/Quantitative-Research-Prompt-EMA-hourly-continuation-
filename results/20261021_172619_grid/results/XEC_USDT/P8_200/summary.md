# EMA Hourly Continuation — XEC/USDT P8_200

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.8634 |
| net_win_rate | 0.5258 |
| gross_profit_factor | 1.0949 |
| gross_win_rate | 0.5258 |
| sharpe_ratio | -0.8716 |
| sortino_ratio | -0.2462 |
| max_drawdown | 0.3525 |
| cagr | -0.1095 |
| net_avg_win | 78.5872 |
| net_avg_loss | -100.9183 |
| avg_hold_time_bars | 42.7680 |
| exposure | 0.7509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
