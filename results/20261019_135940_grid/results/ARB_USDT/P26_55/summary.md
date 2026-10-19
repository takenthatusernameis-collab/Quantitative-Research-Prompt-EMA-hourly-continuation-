# EMA Hourly Continuation — ARB/USDT P26_55

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 870 |
| net_profit_factor | 0.4336 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8469 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -6.6894 |
| sortino_ratio | -2.7769 |
| max_drawdown | 0.9689 |
| cagr | -0.7479 |
| net_avg_win | 18.5849 |
| net_avg_loss | -36.3086 |
| avg_hold_time_bars | 4.4839 |
| exposure | 0.1773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
