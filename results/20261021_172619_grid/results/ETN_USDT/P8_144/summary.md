# EMA Hourly Continuation — ETN/USDT P8_144

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6282 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.7543 |
| gross_win_rate | 0.4364 |
| sharpe_ratio | -3.3274 |
| sortino_ratio | -1.1162 |
| max_drawdown | 0.6848 |
| cagr | -0.4028 |
| net_avg_win | 54.2648 |
| net_avg_loss | -66.8961 |
| avg_hold_time_bars | 22.3771 |
| exposure | 0.5737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
