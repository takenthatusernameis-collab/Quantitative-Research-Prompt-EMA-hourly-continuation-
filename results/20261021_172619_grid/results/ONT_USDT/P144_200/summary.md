# EMA Hourly Continuation — ONT/USDT P144_200

**Symbol:** ONT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.5825 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8197 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -2.3718 |
| sortino_ratio | -0.4938 |
| max_drawdown | 0.4688 |
| cagr | -0.2021 |
| net_avg_win | 62.4589 |
| net_avg_loss | -88.8989 |
| avg_hold_time_bars | 5.5654 |
| exposure | 0.0539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
