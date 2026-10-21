# EMA Hourly Continuation — ZRX/USDT P50_144

**Symbol:** ZRX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8055 |
| net_win_rate | 0.5218 |
| gross_profit_factor | 1.0592 |
| gross_win_rate | 0.5218 |
| sharpe_ratio | -1.2364 |
| sortino_ratio | -0.3611 |
| max_drawdown | 0.3682 |
| cagr | -0.1536 |
| net_avg_win | 65.9073 |
| net_avg_loss | -89.3009 |
| avg_hold_time_bars | 14.1092 |
| exposure | 0.2642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
