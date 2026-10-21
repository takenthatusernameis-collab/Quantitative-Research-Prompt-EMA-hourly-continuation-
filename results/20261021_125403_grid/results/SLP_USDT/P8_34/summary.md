# EMA Hourly Continuation — SLP/USDT P8_34

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 828 |
| net_profit_factor | 0.7455 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9860 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -3.0165 |
| sortino_ratio | -1.2425 |
| max_drawdown | 0.7631 |
| cagr | -0.4343 |
| net_avg_win | 55.0443 |
| net_avg_loss | -70.6900 |
| avg_hold_time_bars | 7.6039 |
| exposure | 0.2862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
