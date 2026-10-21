# EMA Hourly Continuation — ETC/USDT P21_200

**Symbol:** ETC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.7995 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.0155 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -1.1549 |
| sortino_ratio | -0.2781 |
| max_drawdown | 0.3485 |
| cagr | -0.1211 |
| net_avg_win | 77.2243 |
| net_avg_loss | -98.6567 |
| avg_hold_time_bars | 47.9647 |
| exposure | 0.6170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
