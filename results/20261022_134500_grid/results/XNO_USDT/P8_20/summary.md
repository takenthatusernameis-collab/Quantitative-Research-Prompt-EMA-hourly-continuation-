# EMA Hourly Continuation — XNO/USDT P8_20

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1812 |
| net_profit_factor | 0.2919 |
| net_win_rate | 0.3538 |
| gross_profit_factor | 0.6379 |
| gross_win_rate | 0.3731 |
| sharpe_ratio | -16.0801 |
| sortino_ratio | -9.7359 |
| max_drawdown | 1.0000 |
| cagr | -0.9931 |
| net_avg_win | 6.4322 |
| net_avg_loss | -12.0606 |
| avg_hold_time_bars | 2.6849 |
| exposure | 0.2211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
