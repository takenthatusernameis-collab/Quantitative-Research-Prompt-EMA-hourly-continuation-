# EMA Hourly Continuation — ID/USDT P12_34

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.5260 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 1.0281 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -7.2760 |
| sortino_ratio | -3.4284 |
| max_drawdown | 0.9854 |
| cagr | -0.8107 |
| net_avg_win | 21.2233 |
| net_avg_loss | -34.1773 |
| avg_hold_time_bars | 5.2725 |
| exposure | 0.2680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
