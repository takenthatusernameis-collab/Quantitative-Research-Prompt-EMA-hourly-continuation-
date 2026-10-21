# EMA Hourly Continuation — AAVE/USDT P20_89

**Symbol:** AAVE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.7587 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9345 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -1.9167 |
| sortino_ratio | -0.5794 |
| max_drawdown | 0.5244 |
| cagr | -0.2343 |
| net_avg_win | 71.0938 |
| net_avg_loss | -86.8727 |
| avg_hold_time_bars | 17.8686 |
| exposure | 0.3647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
