# EMA Hourly Continuation — WEMIX/USDT P20_34

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1653 |
| net_profit_factor | 0.1379 |
| net_win_rate | 0.2674 |
| gross_profit_factor | 0.3737 |
| gross_win_rate | 0.2995 |
| sharpe_ratio | -20.6864 |
| sortino_ratio | -12.3791 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 3.6188 |
| net_avg_loss | -9.5785 |
| avg_hold_time_bars | 2.6842 |
| exposure | 0.2017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
