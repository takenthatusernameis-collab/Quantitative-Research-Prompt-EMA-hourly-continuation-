# EMA Hourly Continuation — API3/USDT P26_34

**Symbol:** API3/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.5908 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8584 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -2.7999 |
| sortino_ratio | -0.6380 |
| max_drawdown | 0.5676 |
| cagr | -0.2559 |
| net_avg_win | 65.2285 |
| net_avg_loss | -92.7989 |
| avg_hold_time_bars | 5.0984 |
| exposure | 0.0589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
