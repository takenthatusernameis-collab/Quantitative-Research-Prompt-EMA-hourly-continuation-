# EMA Hourly Continuation — SQD/USDT P50_144

**Symbol:** SQD/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7434 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 1.0593 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -2.3053 |
| sortino_ratio | -0.7276 |
| max_drawdown | 0.5971 |
| cagr | -0.2932 |
| net_avg_win | 67.6142 |
| net_avg_loss | -91.7023 |
| avg_hold_time_bars | 11.6667 |
| exposure | 0.2665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
