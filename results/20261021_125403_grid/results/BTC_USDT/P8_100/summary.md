# EMA Hourly Continuation — BTC/USDT P8_100

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.6541 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9556 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -2.5715 |
| sortino_ratio | -0.7666 |
| max_drawdown | 0.6364 |
| cagr | -0.2952 |
| net_avg_win | 48.9473 |
| net_avg_loss | -73.6222 |
| avg_hold_time_bars | 34.2154 |
| exposure | 0.6734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
