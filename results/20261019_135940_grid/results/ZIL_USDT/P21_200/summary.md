# EMA Hourly Continuation — ZIL/USDT P21_200

**Symbol:** ZIL/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6976 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0491 |
| gross_win_rate | 0.5156 |
| sharpe_ratio | -2.1128 |
| sortino_ratio | -0.5795 |
| max_drawdown | 0.5481 |
| cagr | -0.2456 |
| net_avg_win | 60.3247 |
| net_avg_loss | -88.2917 |
| avg_hold_time_bars | 35.5651 |
| exposure | 0.6208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
