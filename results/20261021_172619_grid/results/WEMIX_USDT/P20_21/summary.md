# EMA Hourly Continuation — WEMIX/USDT P20_21

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 117 |
| net_profit_factor | 0.3845 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.5364 |
| gross_win_rate | 0.3333 |
| sharpe_ratio | -3.3319 |
| sortino_ratio | -0.5130 |
| max_drawdown | 0.4574 |
| cagr | -0.2134 |
| net_avg_win | 72.5295 |
| net_avg_loss | -94.3104 |
| avg_hold_time_bars | 10.2906 |
| exposure | 0.0547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
