# EMA Hourly Continuation — ZKJ/USDT P55_200

**Symbol:** ZKJ/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.2304 |
| net_win_rate | 0.3524 |
| gross_profit_factor | 0.5863 |
| gross_win_rate | 0.4048 |
| sharpe_ratio | -5.5649 |
| sortino_ratio | -1.1712 |
| max_drawdown | 0.7858 |
| cagr | -0.4486 |
| net_avg_win | 31.3743 |
| net_avg_loss | -74.1076 |
| avg_hold_time_bars | 83.7000 |
| exposure | 0.7990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
