# EMA Hourly Continuation — BCH/USDT P8_21

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1638 |
| net_profit_factor | 0.2599 |
| net_win_rate | 0.3864 |
| gross_profit_factor | 0.7777 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -15.5823 |
| sortino_ratio | -9.0140 |
| max_drawdown | 1.0000 |
| cagr | -0.9919 |
| net_avg_win | 5.5482 |
| net_avg_loss | -13.4447 |
| avg_hold_time_bars | 3.0171 |
| exposure | 0.2246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
