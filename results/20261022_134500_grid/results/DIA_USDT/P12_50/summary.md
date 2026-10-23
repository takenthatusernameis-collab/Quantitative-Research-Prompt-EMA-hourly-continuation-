# EMA Hourly Continuation — DIA/USDT P12_50

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1045 |
| net_profit_factor | 0.4831 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.8162 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -6.7509 |
| sortino_ratio | -3.0555 |
| max_drawdown | 0.9763 |
| cagr | -0.7723 |
| net_avg_win | 19.4120 |
| net_avg_loss | -32.8425 |
| avg_hold_time_bars | 7.3416 |
| exposure | 0.3472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
