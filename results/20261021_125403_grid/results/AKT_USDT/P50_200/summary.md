# EMA Hourly Continuation — AKT/USDT P50_200

**Symbol:** AKT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.8471 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0069 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -0.8777 |
| sortino_ratio | -0.2260 |
| max_drawdown | 0.2347 |
| cagr | -0.1010 |
| net_avg_win | 79.7550 |
| net_avg_loss | -95.9165 |
| avg_hold_time_bars | 24.3313 |
| exposure | 0.3572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
