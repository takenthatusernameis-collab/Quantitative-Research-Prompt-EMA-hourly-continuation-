# EMA Hourly Continuation — ZEN/USDT P21_200

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7233 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0059 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.8451 |
| sortino_ratio | -0.4744 |
| max_drawdown | 0.4873 |
| cagr | -0.2039 |
| net_avg_win | 67.8085 |
| net_avg_loss | -94.3167 |
| avg_hold_time_bars | 44.7493 |
| exposure | 0.6814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
