# EMA Hourly Continuation — WEMIX/USDT P55_89

**Symbol:** WEMIX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.5231 |
| net_win_rate | 0.4078 |
| gross_profit_factor | 0.7009 |
| gross_win_rate | 0.4078 |
| sharpe_ratio | -3.3631 |
| sortino_ratio | -0.7619 |
| max_drawdown | 0.5878 |
| cagr | -0.2974 |
| net_avg_win | 61.9954 |
| net_avg_loss | -81.6266 |
| avg_hold_time_bars | 8.8627 |
| exposure | 0.1027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
