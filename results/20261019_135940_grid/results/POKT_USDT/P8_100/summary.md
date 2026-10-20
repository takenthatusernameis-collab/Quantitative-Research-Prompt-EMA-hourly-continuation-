# EMA Hourly Continuation — POKT/USDT P8_100

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 851 |
| net_profit_factor | 0.5923 |
| net_win_rate | 0.4207 |
| gross_profit_factor | 0.8784 |
| gross_win_rate | 0.4277 |
| sharpe_ratio | -6.1854 |
| sortino_ratio | -2.5193 |
| max_drawdown | 0.9549 |
| cagr | -0.7041 |
| net_avg_win | 38.7010 |
| net_avg_loss | -47.4472 |
| avg_hold_time_bars | 16.6980 |
| exposure | 0.6430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
