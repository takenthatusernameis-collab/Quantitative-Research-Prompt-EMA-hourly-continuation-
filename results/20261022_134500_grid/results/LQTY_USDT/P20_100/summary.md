# EMA Hourly Continuation — LQTY/USDT P20_100

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.6060 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.8541 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -4.2210 |
| sortino_ratio | -1.5340 |
| max_drawdown | 0.8447 |
| cagr | -0.5115 |
| net_avg_win | 43.2831 |
| net_avg_loss | -58.2808 |
| avg_hold_time_bars | 15.2269 |
| exposure | 0.4555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
