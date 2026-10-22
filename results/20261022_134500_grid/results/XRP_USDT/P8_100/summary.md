# EMA Hourly Continuation — XRP/USDT P8_100

**Symbol:** XRP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.5249 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 1.0149 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -5.8432 |
| sortino_ratio | -2.1895 |
| max_drawdown | 0.9455 |
| cagr | -0.6712 |
| net_avg_win | 31.0525 |
| net_avg_loss | -50.5349 |
| avg_hold_time_bars | 18.8828 |
| exposure | 0.6223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
