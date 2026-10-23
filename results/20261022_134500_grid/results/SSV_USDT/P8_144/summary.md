# EMA Hourly Continuation — SSV/USDT P8_144

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.6598 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -2.6411 |
| sortino_ratio | -0.7560 |
| max_drawdown | 0.6353 |
| cagr | -0.3051 |
| net_avg_win | 58.5457 |
| net_avg_loss | -79.9035 |
| avg_hold_time_bars | 41.8000 |
| exposure | 0.7944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
