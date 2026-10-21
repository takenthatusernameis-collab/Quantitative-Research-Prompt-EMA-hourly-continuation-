# EMA Hourly Continuation — PHA/USDT P144_200

**Symbol:** PHA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.6249 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 0.8010 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -2.0192 |
| sortino_ratio | -0.3880 |
| max_drawdown | 0.3775 |
| cagr | -0.1636 |
| net_avg_win | 74.3643 |
| net_avg_loss | -94.5038 |
| avg_hold_time_bars | 6.7158 |
| exposure | 0.0559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
