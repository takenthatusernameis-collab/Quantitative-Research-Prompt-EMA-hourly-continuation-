# EMA Hourly Continuation — ZIL/USDT P144_200

**Symbol:** ZIL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.7488 |
| net_win_rate | 0.5286 |
| gross_profit_factor | 1.0756 |
| gross_win_rate | 0.5286 |
| sharpe_ratio | -1.1387 |
| sortino_ratio | -0.2381 |
| max_drawdown | 0.3164 |
| cagr | -0.1037 |
| net_avg_win | 64.5687 |
| net_avg_loss | -96.6780 |
| avg_hold_time_bars | 6.4381 |
| exposure | 0.0615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
