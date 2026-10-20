# EMA Hourly Continuation — RLC/USDT P144_200

**Symbol:** RLC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.4840 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8641 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -4.2782 |
| sortino_ratio | -1.2323 |
| max_drawdown | 0.7688 |
| cagr | -0.4382 |
| net_avg_win | 38.7925 |
| net_avg_loss | -67.0891 |
| avg_hold_time_bars | 4.8645 |
| exposure | 0.0898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
