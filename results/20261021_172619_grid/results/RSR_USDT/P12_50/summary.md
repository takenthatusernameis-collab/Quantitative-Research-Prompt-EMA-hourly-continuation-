# EMA Hourly Continuation — RSR/USDT P12_50

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.7714 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9503 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.3347 |
| sortino_ratio | -0.8656 |
| max_drawdown | 0.6467 |
| cagr | -0.3291 |
| net_avg_win | 65.5218 |
| net_avg_loss | -79.3424 |
| avg_hold_time_bars | 9.5659 |
| exposure | 0.2935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
