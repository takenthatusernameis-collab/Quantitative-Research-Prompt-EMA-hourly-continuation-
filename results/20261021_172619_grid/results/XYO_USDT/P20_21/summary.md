# EMA Hourly Continuation — XYO/USDT P20_21

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.4388 |
| net_win_rate | 0.3990 |
| gross_profit_factor | 0.6977 |
| gross_win_rate | 0.3990 |
| sharpe_ratio | -3.8022 |
| sortino_ratio | -0.7753 |
| max_drawdown | 0.6036 |
| cagr | -0.3027 |
| net_avg_win | 57.6537 |
| net_avg_loss | -87.2392 |
| avg_hold_time_bars | 5.7734 |
| exposure | 0.0530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
