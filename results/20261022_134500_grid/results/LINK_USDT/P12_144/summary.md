# EMA Hourly Continuation — LINK/USDT P12_144

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7394 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0953 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -2.2347 |
| sortino_ratio | -0.6896 |
| max_drawdown | 0.6007 |
| cagr | -0.2809 |
| net_avg_win | 64.4243 |
| net_avg_loss | -93.1376 |
| avg_hold_time_bars | 29.5417 |
| exposure | 0.6445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
