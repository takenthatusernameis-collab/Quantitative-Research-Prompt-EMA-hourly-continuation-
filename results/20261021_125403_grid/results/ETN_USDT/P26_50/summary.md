# EMA Hourly Continuation — ETN/USDT P26_50

**Symbol:** ETN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.4748 |
| net_win_rate | 0.3932 |
| gross_profit_factor | 0.6223 |
| gross_win_rate | 0.3932 |
| sharpe_ratio | -4.1412 |
| sortino_ratio | -1.0989 |
| max_drawdown | 0.6596 |
| cagr | -0.3984 |
| net_avg_win | 51.1418 |
| net_avg_loss | -69.8072 |
| avg_hold_time_bars | 8.5695 |
| exposure | 0.1373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
