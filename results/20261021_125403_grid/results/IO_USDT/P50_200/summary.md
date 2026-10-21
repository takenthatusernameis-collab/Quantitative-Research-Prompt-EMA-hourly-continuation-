# EMA Hourly Continuation — IO/USDT P50_200

**Symbol:** IO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.8435 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 0.9914 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -0.9576 |
| sortino_ratio | -0.2383 |
| max_drawdown | 0.2971 |
| cagr | -0.1054 |
| net_avg_win | 88.2654 |
| net_avg_loss | -103.1772 |
| avg_hold_time_bars | 26.8028 |
| exposure | 0.3685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
