# EMA Hourly Continuation — APE/USDT P50_100

**Symbol:** APE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.5251 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9221 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -4.5736 |
| sortino_ratio | -1.6662 |
| max_drawdown | 0.8684 |
| cagr | -0.5493 |
| net_avg_win | 29.7898 |
| net_avg_loss | -52.4825 |
| avg_hold_time_bars | 6.1557 |
| exposure | 0.1869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
