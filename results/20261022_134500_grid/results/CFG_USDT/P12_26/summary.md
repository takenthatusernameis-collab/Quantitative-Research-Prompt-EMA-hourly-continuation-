# EMA Hourly Continuation — CFG/USDT P12_26

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1186 |
| net_profit_factor | 0.3099 |
| net_win_rate | 0.4039 |
| gross_profit_factor | 0.6407 |
| gross_win_rate | 0.4157 |
| sharpe_ratio | -10.0687 |
| sortino_ratio | -4.8833 |
| max_drawdown | 0.9978 |
| cagr | -0.9127 |
| net_avg_win | 9.3554 |
| net_avg_loss | -20.4517 |
| avg_hold_time_bars | 6.6509 |
| exposure | 0.3585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
