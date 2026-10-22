# EMA Hourly Continuation — BDX/USDT P55_100

**Symbol:** BDX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.1711 |
| net_win_rate | 0.2599 |
| gross_profit_factor | 0.4572 |
| gross_win_rate | 0.3273 |
| sharpe_ratio | -18.1965 |
| sortino_ratio | -9.3810 |
| max_drawdown | 1.0000 |
| cagr | -0.9946 |
| net_avg_win | 7.1431 |
| net_avg_loss | -14.6590 |
| avg_hold_time_bars | 3.0225 |
| exposure | 0.1528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
