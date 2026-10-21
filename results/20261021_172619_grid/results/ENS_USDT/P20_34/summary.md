# EMA Hourly Continuation — ENS/USDT P20_34

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7036 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9977 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -2.1401 |
| sortino_ratio | -0.5684 |
| max_drawdown | 0.4954 |
| cagr | -0.2302 |
| net_avg_win | 66.8482 |
| net_avg_loss | -94.4579 |
| avg_hold_time_bars | 5.4344 |
| exposure | 0.0847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
