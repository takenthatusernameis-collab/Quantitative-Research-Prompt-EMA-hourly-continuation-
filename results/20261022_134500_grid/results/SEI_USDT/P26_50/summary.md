# EMA Hourly Continuation — SEI/USDT P26_50

**Symbol:** SEI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.4852 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8711 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -7.3697 |
| sortino_ratio | -3.1634 |
| max_drawdown | 0.9819 |
| cagr | -0.7938 |
| net_avg_win | 21.5532 |
| net_avg_loss | -37.4392 |
| avg_hold_time_bars | 3.6471 |
| exposure | 0.1555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
