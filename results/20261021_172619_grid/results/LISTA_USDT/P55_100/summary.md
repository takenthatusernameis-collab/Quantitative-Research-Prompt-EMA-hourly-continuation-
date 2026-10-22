# EMA Hourly Continuation — LISTA/USDT P55_100

**Symbol:** LISTA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.6752 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8688 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -2.3927 |
| sortino_ratio | -0.6697 |
| max_drawdown | 0.5221 |
| cagr | -0.2654 |
| net_avg_win | 63.4963 |
| net_avg_loss | -82.7196 |
| avg_hold_time_bars | 9.5794 |
| exposure | 0.1682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
