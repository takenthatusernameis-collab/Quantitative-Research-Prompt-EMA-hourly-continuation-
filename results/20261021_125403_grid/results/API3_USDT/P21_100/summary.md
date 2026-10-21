# EMA Hourly Continuation — API3/USDT P21_100

**Symbol:** API3/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.8148 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0196 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -1.4230 |
| sortino_ratio | -0.4556 |
| max_drawdown | 0.4394 |
| cagr | -0.1900 |
| net_avg_win | 71.7269 |
| net_avg_loss | -90.1815 |
| avg_hold_time_bars | 17.3313 |
| exposure | 0.3923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
