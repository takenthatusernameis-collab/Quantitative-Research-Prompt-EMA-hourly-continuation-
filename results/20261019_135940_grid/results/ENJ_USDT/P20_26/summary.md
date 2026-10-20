# EMA Hourly Continuation — ENJ/USDT P20_26

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1198 |
| net_profit_factor | 0.2376 |
| net_win_rate | 0.3748 |
| gross_profit_factor | 0.7203 |
| gross_win_rate | 0.4249 |
| sharpe_ratio | -13.6859 |
| sortino_ratio | -6.8941 |
| max_drawdown | 0.9999 |
| cagr | -0.9720 |
| net_avg_win | 6.9419 |
| net_avg_loss | -17.5109 |
| avg_hold_time_bars | 1.9048 |
| exposure | 0.1037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
