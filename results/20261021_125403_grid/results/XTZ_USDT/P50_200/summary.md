# EMA Hourly Continuation — XTZ/USDT P50_200

**Symbol:** XTZ/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.7990 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0331 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.1982 |
| sortino_ratio | -0.3077 |
| max_drawdown | 0.3268 |
| cagr | -0.1325 |
| net_avg_win | 73.1758 |
| net_avg_loss | -95.0868 |
| avg_hold_time_bars | 25.7688 |
| exposure | 0.3748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
