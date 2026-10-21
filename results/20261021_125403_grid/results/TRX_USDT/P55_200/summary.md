# EMA Hourly Continuation — TRX/USDT P55_200

**Symbol:** TRX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.5568 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0105 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -2.9550 |
| sortino_ratio | -0.6966 |
| max_drawdown | 0.5598 |
| cagr | -0.2761 |
| net_avg_win | 51.3450 |
| net_avg_loss | -94.2942 |
| avg_hold_time_bars | 23.0037 |
| exposure | 0.2813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
