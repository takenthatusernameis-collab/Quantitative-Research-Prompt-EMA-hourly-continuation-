# EMA Hourly Continuation — AVAX/USDT P50_200

**Symbol:** AVAX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7359 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9206 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -1.4969 |
| sortino_ratio | -0.3426 |
| max_drawdown | 0.3481 |
| cagr | -0.1459 |
| net_avg_win | 73.5094 |
| net_avg_loss | -93.1309 |
| avg_hold_time_bars | 31.2257 |
| exposure | 0.3648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
