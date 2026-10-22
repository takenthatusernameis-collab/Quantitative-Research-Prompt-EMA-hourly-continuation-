# EMA Hourly Continuation — ZRO/USDT P34_55

**Symbol:** ZRO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 842 |
| net_profit_factor | 0.5650 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -5.8874 |
| sortino_ratio | -2.4912 |
| max_drawdown | 0.9427 |
| cagr | -0.7055 |
| net_avg_win | 30.4416 |
| net_avg_loss | -49.2267 |
| avg_hold_time_bars | 3.1449 |
| exposure | 0.1296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
