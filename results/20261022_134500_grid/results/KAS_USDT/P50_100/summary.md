# EMA Hourly Continuation — KAS/USDT P50_100

**Symbol:** KAS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.4435 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.8318 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -6.1816 |
| sortino_ratio | -2.2418 |
| max_drawdown | 0.9382 |
| cagr | -0.6670 |
| net_avg_win | 25.3065 |
| net_avg_loss | -46.3727 |
| avg_hold_time_bars | 5.3906 |
| exposure | 0.1612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
