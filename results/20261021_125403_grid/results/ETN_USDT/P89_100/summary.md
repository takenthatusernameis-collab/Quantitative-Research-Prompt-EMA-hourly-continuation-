# EMA Hourly Continuation — ETN/USDT P89_100

**Symbol:** ETN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 105 |
| net_profit_factor | 0.4182 |
| net_win_rate | 0.3619 |
| gross_profit_factor | 0.5500 |
| gross_win_rate | 0.3619 |
| sharpe_ratio | -2.8607 |
| sortino_ratio | -0.4518 |
| max_drawdown | 0.3632 |
| cagr | -0.1899 |
| net_avg_win | 67.6557 |
| net_avg_loss | -91.7559 |
| avg_hold_time_bars | 6.5619 |
| exposure | 0.0374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
