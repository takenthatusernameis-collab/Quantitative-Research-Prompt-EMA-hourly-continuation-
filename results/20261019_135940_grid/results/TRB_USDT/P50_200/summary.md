# EMA Hourly Continuation — TRB/USDT P50_200

**Symbol:** TRB/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.5772 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8701 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -3.6815 |
| sortino_ratio | -1.0603 |
| max_drawdown | 0.7331 |
| cagr | -0.4001 |
| net_avg_win | 51.2504 |
| net_avg_loss | -72.9186 |
| avg_hold_time_bars | 19.5210 |
| exposure | 0.3781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
