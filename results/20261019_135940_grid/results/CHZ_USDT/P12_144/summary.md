# EMA Hourly Continuation — CHZ/USDT P12_144

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7561 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0542 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.7632 |
| sortino_ratio | -0.5213 |
| max_drawdown | 0.4868 |
| cagr | -0.2192 |
| net_avg_win | 64.9281 |
| net_avg_loss | -88.6762 |
| avg_hold_time_bars | 35.2414 |
| exposure | 0.6968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
