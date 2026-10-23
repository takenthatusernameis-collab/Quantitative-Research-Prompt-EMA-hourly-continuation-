# EMA Hourly Continuation — SKL/USDT P89_100

**Symbol:** SKL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.3377 |
| net_win_rate | 0.4178 |
| gross_profit_factor | 0.7883 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -7.7833 |
| sortino_ratio | -2.7002 |
| max_drawdown | 0.9684 |
| cagr | -0.7449 |
| net_avg_win | 20.2160 |
| net_avg_loss | -42.9673 |
| avg_hold_time_bars | 2.2175 |
| exposure | 0.0589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
