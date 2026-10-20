# EMA Hourly Continuation — 1INCH/USDT P144_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.4819 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.9877 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -4.9644 |
| sortino_ratio | -1.4033 |
| max_drawdown | 0.8399 |
| cagr | -0.5140 |
| net_avg_win | 40.9540 |
| net_avg_loss | -74.4145 |
| avg_hold_time_bars | 4.5356 |
| exposure | 0.0839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
