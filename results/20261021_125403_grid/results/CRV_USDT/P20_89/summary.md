# EMA Hourly Continuation — CRV/USDT P20_89

**Symbol:** CRV/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.8589 |
| net_win_rate | 0.5144 |
| gross_profit_factor | 1.0606 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -1.0727 |
| sortino_ratio | -0.3399 |
| max_drawdown | 0.3555 |
| cagr | -0.1472 |
| net_avg_win | 80.2234 |
| net_avg_loss | -98.9482 |
| avg_hold_time_bars | 14.8477 |
| exposure | 0.3280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
