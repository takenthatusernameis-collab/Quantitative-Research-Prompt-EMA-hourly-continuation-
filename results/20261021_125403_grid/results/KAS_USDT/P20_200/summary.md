# EMA Hourly Continuation — KAS/USDT P20_200

**Symbol:** KAS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7852 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9503 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.3206 |
| sortino_ratio | -0.3458 |
| max_drawdown | 0.3488 |
| cagr | -0.1481 |
| net_avg_win | 72.9556 |
| net_avg_loss | -90.2010 |
| avg_hold_time_bars | 37.9733 |
| exposure | 0.5817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
