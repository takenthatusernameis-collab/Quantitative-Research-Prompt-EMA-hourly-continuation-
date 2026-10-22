# EMA Hourly Continuation — RAY/USDT P144_200

**Symbol:** RAY/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5191 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8966 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -4.2593 |
| sortino_ratio | -1.2053 |
| max_drawdown | 0.7693 |
| cagr | -0.4401 |
| net_avg_win | 45.4852 |
| net_avg_loss | -73.1541 |
| avg_hold_time_bars | 4.5550 |
| exposure | 0.0828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
