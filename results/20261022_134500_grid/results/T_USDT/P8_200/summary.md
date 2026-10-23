# EMA Hourly Continuation — T/USDT P8_200

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.8036 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1186 |
| gross_win_rate | 0.5349 |
| sharpe_ratio | -1.1196 |
| sortino_ratio | -0.2759 |
| max_drawdown | 0.3423 |
| cagr | -0.1226 |
| net_avg_win | 71.8372 |
| net_avg_loss | -101.4436 |
| avg_hold_time_bars | 59.2392 |
| exposure | 0.8069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
