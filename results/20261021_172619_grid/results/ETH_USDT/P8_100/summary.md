# EMA Hourly Continuation — ETH/USDT P8_100

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7593 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0091 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -1.6001 |
| sortino_ratio | -0.4400 |
| max_drawdown | 0.4323 |
| cagr | -0.1827 |
| net_avg_win | 67.4302 |
| net_avg_loss | -90.7551 |
| avg_hold_time_bars | 40.2636 |
| exposure | 0.6735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
