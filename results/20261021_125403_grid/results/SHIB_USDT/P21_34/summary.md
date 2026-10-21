# EMA Hourly Continuation — SHIB/USDT P21_34

**Symbol:** SHIB/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.7261 |
| net_win_rate | 0.5158 |
| gross_profit_factor | 1.0619 |
| gross_win_rate | 0.5158 |
| sharpe_ratio | -1.4796 |
| sortino_ratio | -0.3173 |
| max_drawdown | 0.3419 |
| cagr | -0.1351 |
| net_avg_win | 71.0350 |
| net_avg_loss | -104.2276 |
| avg_hold_time_bars | 5.3665 |
| exposure | 0.0539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
