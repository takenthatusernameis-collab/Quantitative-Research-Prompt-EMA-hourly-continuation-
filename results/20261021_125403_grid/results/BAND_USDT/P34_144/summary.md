# EMA Hourly Continuation — BAND/USDT P34_144

**Symbol:** BAND/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7048 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9029 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -2.0532 |
| sortino_ratio | -0.5647 |
| max_drawdown | 0.4917 |
| cagr | -0.2293 |
| net_avg_win | 64.2469 |
| net_avg_loss | -83.2479 |
| avg_hold_time_bars | 23.8133 |
| exposure | 0.4041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
