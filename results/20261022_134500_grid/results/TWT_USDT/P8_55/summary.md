# EMA Hourly Continuation — TWT/USDT P8_55

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1143 |
| net_profit_factor | 0.4096 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.7945 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -6.9907 |
| sortino_ratio | -3.3105 |
| max_drawdown | 0.9837 |
| cagr | -0.8043 |
| net_avg_win | 12.8747 |
| net_avg_loss | -27.1733 |
| avg_hold_time_bars | 9.7200 |
| exposure | 0.5050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
