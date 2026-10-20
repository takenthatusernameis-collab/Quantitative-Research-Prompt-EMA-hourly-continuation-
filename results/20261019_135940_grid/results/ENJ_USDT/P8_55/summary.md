# EMA Hourly Continuation — ENJ/USDT P8_55

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1073 |
| net_profit_factor | 0.5808 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.9304 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -6.1044 |
| sortino_ratio | -2.8122 |
| max_drawdown | 0.9676 |
| cagr | -0.7432 |
| net_avg_win | 27.0141 |
| net_avg_loss | -39.9827 |
| avg_hold_time_bars | 9.7810 |
| exposure | 0.4770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
