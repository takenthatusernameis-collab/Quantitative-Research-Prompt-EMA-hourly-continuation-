# EMA Hourly Continuation — ILV/USDT P8_34

**Symbol:** ILV/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 812 |
| net_profit_factor | 0.7463 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 0.9881 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -2.4907 |
| sortino_ratio | -1.0187 |
| max_drawdown | 0.7080 |
| cagr | -0.3732 |
| net_avg_win | 49.6574 |
| net_avg_loss | -67.5320 |
| avg_hold_time_bars | 7.6281 |
| exposure | 0.2815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
