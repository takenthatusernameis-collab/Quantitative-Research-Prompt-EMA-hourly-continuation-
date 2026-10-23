# EMA Hourly Continuation — BAND/USDT P34_89

**Symbol:** BAND/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.5866 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9487 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -4.3095 |
| sortino_ratio | -1.5267 |
| max_drawdown | 0.8478 |
| cagr | -0.5170 |
| net_avg_win | 39.4902 |
| net_avg_loss | -61.2390 |
| avg_hold_time_bars | 9.5347 |
| exposure | 0.2735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
