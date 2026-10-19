# EMA Hourly Continuation — CRV/USDT P8_89

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.6439 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9341 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -3.9002 |
| sortino_ratio | -1.3858 |
| max_drawdown | 0.8149 |
| cagr | -0.4846 |
| net_avg_win | 49.0225 |
| net_avg_loss | -66.7591 |
| avg_hold_time_bars | 22.9453 |
| exposure | 0.6675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
