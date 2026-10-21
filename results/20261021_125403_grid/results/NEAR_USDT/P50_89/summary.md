# EMA Hourly Continuation — NEAR/USDT P50_89

**Symbol:** NEAR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.6999 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9075 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -1.7462 |
| sortino_ratio | -0.4206 |
| max_drawdown | 0.3877 |
| cagr | -0.1751 |
| net_avg_win | 65.2422 |
| net_avg_loss | -86.8765 |
| avg_hold_time_bars | 6.7711 |
| exposure | 0.0874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
