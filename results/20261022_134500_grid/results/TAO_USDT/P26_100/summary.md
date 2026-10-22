# EMA Hourly Continuation — TAO/USDT P26_100

**Symbol:** TAO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9576 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -3.6087 |
| sortino_ratio | -1.3081 |
| max_drawdown | 0.8068 |
| cagr | -0.4702 |
| net_avg_win | 50.5202 |
| net_avg_loss | -71.4029 |
| avg_hold_time_bars | 10.9119 |
| exposure | 0.3323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
