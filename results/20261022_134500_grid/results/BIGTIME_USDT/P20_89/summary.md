# EMA Hourly Continuation — BIGTIME/USDT P20_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.6902 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0055 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -3.0138 |
| sortino_ratio | -1.0887 |
| max_drawdown | 0.7404 |
| cagr | -0.4049 |
| net_avg_win | 49.8899 |
| net_avg_loss | -70.9742 |
| avg_hold_time_bars | 14.3419 |
| exposure | 0.4271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
