# EMA Hourly Continuation — SUI/USDT P144_200

**Symbol:** SUI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.4148 |
| net_win_rate | 0.4153 |
| gross_profit_factor | 0.7200 |
| gross_win_rate | 0.4272 |
| sharpe_ratio | -5.6839 |
| sortino_ratio | -1.6320 |
| max_drawdown | 0.8753 |
| cagr | -0.5624 |
| net_avg_win | 35.6171 |
| net_avg_loss | -60.9885 |
| avg_hold_time_bars | 3.9427 |
| exposure | 0.0751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
