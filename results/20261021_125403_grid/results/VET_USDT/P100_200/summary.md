# EMA Hourly Continuation — VET/USDT P100_200

**Symbol:** VET/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.7612 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0028 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.2560 |
| sortino_ratio | -0.2757 |
| max_drawdown | 0.2926 |
| cagr | -0.1196 |
| net_avg_win | 73.9368 |
| net_avg_loss | -98.8092 |
| avg_hold_time_bars | 14.8248 |
| exposure | 0.1577 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
