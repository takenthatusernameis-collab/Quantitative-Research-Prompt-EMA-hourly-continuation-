# EMA Hourly Continuation — DEEP/USDT P20_200

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.6807 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8680 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -2.1308 |
| sortino_ratio | -0.5389 |
| max_drawdown | 0.4160 |
| cagr | -0.2280 |
| net_avg_win | 70.4676 |
| net_avg_loss | -91.6044 |
| avg_hold_time_bars | 45.8168 |
| exposure | 0.6797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
