# EMA Hourly Continuation — AVA/USDT P21_34

**Symbol:** AVA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.6376 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9422 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -2.6756 |
| sortino_ratio | -0.7004 |
| max_drawdown | 0.5935 |
| cagr | -0.2742 |
| net_avg_win | 60.7916 |
| net_avg_loss | -88.6953 |
| avg_hold_time_bars | 5.1355 |
| exposure | 0.0775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
