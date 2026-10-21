# EMA Hourly Continuation — QNT/USDT P8_100

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.8132 |
| net_win_rate | 0.5179 |
| gross_profit_factor | 1.0541 |
| gross_win_rate | 0.5179 |
| sharpe_ratio | -1.4965 |
| sortino_ratio | -0.5342 |
| max_drawdown | 0.5022 |
| cagr | -0.2191 |
| net_avg_win | 63.1336 |
| net_avg_loss | -83.3893 |
| avg_hold_time_bars | 20.5617 |
| exposure | 0.5757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
