# EMA Hourly Continuation — ETN/USDT P55_144

**Symbol:** ETN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.4509 |
| net_win_rate | 0.3892 |
| gross_profit_factor | 0.6726 |
| gross_win_rate | 0.4008 |
| sharpe_ratio | -6.8177 |
| sortino_ratio | -2.3844 |
| max_drawdown | 0.9201 |
| cagr | -0.6917 |
| net_avg_win | 37.2289 |
| net_avg_loss | -52.6073 |
| avg_hold_time_bars | 8.3988 |
| exposure | 0.2368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
