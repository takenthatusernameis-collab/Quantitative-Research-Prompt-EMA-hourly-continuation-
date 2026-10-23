# EMA Hourly Continuation — KNC/USDT P8_100

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.6221 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9489 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -3.7433 |
| sortino_ratio | -1.2321 |
| max_drawdown | 0.7798 |
| cagr | -0.4469 |
| net_avg_win | 49.5827 |
| net_avg_loss | -69.1992 |
| avg_hold_time_bars | 28.1808 |
| exposure | 0.7084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
