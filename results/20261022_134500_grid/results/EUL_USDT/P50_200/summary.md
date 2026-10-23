# EMA Hourly Continuation — EUL/USDT P50_200

**Symbol:** EUL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.5128 |
| net_win_rate | 0.4154 |
| gross_profit_factor | 0.7221 |
| gross_win_rate | 0.4229 |
| sharpe_ratio | -4.0730 |
| sortino_ratio | -1.1451 |
| max_drawdown | 0.7525 |
| cagr | -0.4205 |
| net_avg_win | 47.0084 |
| net_avg_loss | -65.1456 |
| avg_hold_time_bars | 17.0647 |
| exposure | 0.3118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
