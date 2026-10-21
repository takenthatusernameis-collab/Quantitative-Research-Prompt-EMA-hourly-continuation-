# EMA Hourly Continuation — ZETA/USDT P34_50

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.5952 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8567 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -3.1337 |
| sortino_ratio | -0.8283 |
| max_drawdown | 0.6237 |
| cagr | -0.3147 |
| net_avg_win | 57.5489 |
| net_avg_loss | -81.6172 |
| avg_hold_time_bars | 5.3149 |
| exposure | 0.0825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
