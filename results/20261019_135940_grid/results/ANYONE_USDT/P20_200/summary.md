# EMA Hourly Continuation — ANYONE/USDT P20_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8144 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9808 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -1.0921 |
| sortino_ratio | -0.2769 |
| max_drawdown | 0.3351 |
| cagr | -0.1223 |
| net_avg_win | 78.9038 |
| net_avg_loss | -96.2044 |
| avg_hold_time_bars | 46.7193 |
| exposure | 0.6728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
