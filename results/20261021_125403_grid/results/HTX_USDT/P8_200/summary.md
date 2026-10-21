# EMA Hourly Continuation — HTX/USDT P8_200

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.6832 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 1.0142 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -2.0491 |
| sortino_ratio | -0.4453 |
| max_drawdown | 0.4762 |
| cagr | -0.1877 |
| net_avg_win | 77.1864 |
| net_avg_loss | -108.2362 |
| avg_hold_time_bars | 78.5279 |
| exposure | 0.8280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
