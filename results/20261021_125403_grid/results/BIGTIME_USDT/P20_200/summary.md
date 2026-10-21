# EMA Hourly Continuation — BIGTIME/USDT P20_200

**Symbol:** BIGTIME/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8512 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9926 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8379 |
| sortino_ratio | -0.2091 |
| max_drawdown | 0.2985 |
| cagr | -0.0940 |
| net_avg_win | 82.4057 |
| net_avg_loss | -96.8088 |
| avg_hold_time_bars | 47.2516 |
| exposure | 0.6543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
