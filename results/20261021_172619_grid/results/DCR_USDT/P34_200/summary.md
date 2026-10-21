# EMA Hourly Continuation — DCR/USDT P34_200

**Symbol:** DCR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7486 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9550 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -1.8027 |
| sortino_ratio | -0.4958 |
| max_drawdown | 0.4868 |
| cagr | -0.2044 |
| net_avg_win | 72.1040 |
| net_avg_loss | -90.3338 |
| avg_hold_time_bars | 25.7888 |
| exposure | 0.4364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
