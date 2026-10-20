# EMA Hourly Continuation — SSV/USDT P20_26

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1292 |
| net_profit_factor | 0.3149 |
| net_win_rate | 0.3916 |
| gross_profit_factor | 0.7655 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -13.0655 |
| sortino_ratio | -6.7107 |
| max_drawdown | 0.9999 |
| cagr | -0.9694 |
| net_avg_win | 9.0818 |
| net_avg_loss | -18.5673 |
| avg_hold_time_bars | 2.1509 |
| exposure | 0.1258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
