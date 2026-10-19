# EMA Hourly Continuation — DOGE/USDT P8_200

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6806 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 1.0175 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -2.4950 |
| sortino_ratio | -0.6681 |
| max_drawdown | 0.5621 |
| cagr | -0.2730 |
| net_avg_win | 66.3380 |
| net_avg_loss | -93.7583 |
| avg_hold_time_bars | 48.5956 |
| exposure | 0.7974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
