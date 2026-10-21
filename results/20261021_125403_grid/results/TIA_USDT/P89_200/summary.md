# EMA Hourly Continuation — TIA/USDT P89_200

**Symbol:** TIA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.7129 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8509 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -1.6853 |
| sortino_ratio | -0.3689 |
| max_drawdown | 0.3867 |
| cagr | -0.1564 |
| net_avg_win | 79.1894 |
| net_avg_loss | -93.8604 |
| avg_hold_time_bars | 15.9370 |
| exposure | 0.1724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
