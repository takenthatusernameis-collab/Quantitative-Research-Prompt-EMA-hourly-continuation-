# EMA Hourly Continuation — ENS/USDT P50_144

**Symbol:** ENS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.7122 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -1.9282 |
| sortino_ratio | -0.5073 |
| max_drawdown | 0.4627 |
| cagr | -0.2086 |
| net_avg_win | 67.8466 |
| net_avg_loss | -86.2210 |
| avg_hold_time_bars | 18.3548 |
| exposure | 0.2845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
