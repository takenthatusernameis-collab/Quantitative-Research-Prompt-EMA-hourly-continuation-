# EMA Hourly Continuation — ZK/USDT P55_200

**Symbol:** ZK/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.7863 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9354 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.2769 |
| sortino_ratio | -0.3329 |
| max_drawdown | 0.3233 |
| cagr | -0.1430 |
| net_avg_win | 73.3841 |
| net_avg_loss | -89.2232 |
| avg_hold_time_bars | 24.4180 |
| exposure | 0.3702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
