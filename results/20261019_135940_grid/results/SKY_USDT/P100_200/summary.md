# EMA Hourly Continuation — SKY/USDT P100_200

**Symbol:** SKY/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.1430 |
| gross_win_rate | 0.5303 |
| sharpe_ratio | -2.0963 |
| sortino_ratio | -0.6010 |
| max_drawdown | 0.5550 |
| cagr | -0.2452 |
| net_avg_win | 68.7661 |
| net_avg_loss | -102.5704 |
| avg_hold_time_bars | 8.5273 |
| exposure | 0.1569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
