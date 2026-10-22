# EMA Hourly Continuation — NOT/USDT P8_26

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.8469 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.0799 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -1.2056 |
| sortino_ratio | -0.4114 |
| max_drawdown | 0.4317 |
| cagr | -0.1749 |
| net_avg_win | 72.9685 |
| net_avg_loss | -93.7775 |
| avg_hold_time_bars | 7.5193 |
| exposure | 0.1918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
