# EMA Hourly Continuation — MOG/USDT P26_200

**Symbol:** MOG/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.7804 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.8996 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -1.3290 |
| sortino_ratio | -0.3267 |
| max_drawdown | 0.3406 |
| cagr | -0.1406 |
| net_avg_win | 79.7092 |
| net_avg_loss | -93.5703 |
| avg_hold_time_bars | 41.7664 |
| exposure | 0.5689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
