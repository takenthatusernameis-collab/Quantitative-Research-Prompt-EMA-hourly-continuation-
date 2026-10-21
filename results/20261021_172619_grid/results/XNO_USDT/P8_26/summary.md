# EMA Hourly Continuation — XNO/USDT P8_26

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6476 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.8824 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -4.3199 |
| sortino_ratio | -1.5879 |
| max_drawdown | 0.8420 |
| cagr | -0.5185 |
| net_avg_win | 52.1845 |
| net_avg_loss | -64.2881 |
| avg_hold_time_bars | 6.1379 |
| exposure | 0.1861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
