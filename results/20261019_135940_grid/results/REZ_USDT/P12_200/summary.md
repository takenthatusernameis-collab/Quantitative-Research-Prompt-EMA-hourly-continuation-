# EMA Hourly Continuation — REZ/USDT P12_200

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8291 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 1.0524 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -1.1823 |
| sortino_ratio | -0.3449 |
| max_drawdown | 0.3969 |
| cagr | -0.1507 |
| net_avg_win | 76.8063 |
| net_avg_loss | -96.3102 |
| avg_hold_time_bars | 37.4684 |
| exposure | 0.7122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
