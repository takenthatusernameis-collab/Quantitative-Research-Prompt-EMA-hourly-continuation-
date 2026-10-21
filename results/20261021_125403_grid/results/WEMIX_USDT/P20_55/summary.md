# EMA Hourly Continuation — WEMIX/USDT P20_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5488 |
| net_win_rate | 0.4075 |
| gross_profit_factor | 0.7266 |
| gross_win_rate | 0.4075 |
| sharpe_ratio | -4.1947 |
| sortino_ratio | -1.1881 |
| max_drawdown | 0.7541 |
| cagr | -0.4240 |
| net_avg_win | 55.9392 |
| net_avg_loss | -70.1086 |
| avg_hold_time_bars | 12.7425 |
| exposure | 0.2317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
