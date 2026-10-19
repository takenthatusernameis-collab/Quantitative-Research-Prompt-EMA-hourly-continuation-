# EMA Hourly Continuation — XLM/USDT P50_200

**Symbol:** XLM/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.5649 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 1.0000 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -3.3567 |
| sortino_ratio | -0.9194 |
| max_drawdown | 0.6864 |
| cagr | -0.3566 |
| net_avg_win | 48.3104 |
| net_avg_loss | -77.3485 |
| avg_hold_time_bars | 23.4222 |
| exposure | 0.4035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
