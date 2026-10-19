# EMA Hourly Continuation — OP/USDT P26_34

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.2157 |
| net_win_rate | 0.3851 |
| gross_profit_factor | 0.6436 |
| gross_win_rate | 0.4140 |
| sharpe_ratio | -12.3817 |
| sortino_ratio | -5.8512 |
| max_drawdown | 0.9995 |
| cagr | -0.9521 |
| net_avg_win | 6.6400 |
| net_avg_loss | -19.2800 |
| avg_hold_time_bars | 1.8977 |
| exposure | 0.0927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
