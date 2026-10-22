# EMA Hourly Continuation — CPOOL/USDT P26_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.7620 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.8870 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -1.7080 |
| sortino_ratio | -0.5205 |
| max_drawdown | 0.5170 |
| cagr | -0.2146 |
| net_avg_win | 66.5035 |
| net_avg_loss | -79.6384 |
| avg_hold_time_bars | 16.5969 |
| exposure | 0.3463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
