# EMA Hourly Continuation — PEPE/USDT P8_34

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1412 |
| net_profit_factor | 0.5558 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8718 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -8.3541 |
| sortino_ratio | -4.3945 |
| max_drawdown | 0.9958 |
| cagr | -0.8855 |
| net_avg_win | 19.5857 |
| net_avg_loss | -28.8831 |
| avg_hold_time_bars | 5.1544 |
| exposure | 0.3308 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
