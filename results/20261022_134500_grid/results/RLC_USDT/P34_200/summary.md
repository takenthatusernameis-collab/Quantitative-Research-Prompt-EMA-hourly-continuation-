# EMA Hourly Continuation — RLC/USDT P34_200

**Symbol:** RLC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.6365 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -2.7935 |
| sortino_ratio | -0.7808 |
| max_drawdown | 0.6175 |
| cagr | -0.3102 |
| net_avg_win | 57.7226 |
| net_avg_loss | -78.7073 |
| avg_hold_time_bars | 28.6742 |
| exposure | 0.5161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
