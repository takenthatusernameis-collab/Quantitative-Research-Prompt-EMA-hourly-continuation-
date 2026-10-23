# EMA Hourly Continuation — ORBS/USDT P26_55

**Symbol:** ORBS/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.4159 |
| net_win_rate | 0.3955 |
| gross_profit_factor | 0.9003 |
| gross_win_rate | 0.4278 |
| sharpe_ratio | -9.8564 |
| sortino_ratio | -4.2382 |
| max_drawdown | 0.9959 |
| cagr | -0.8866 |
| net_avg_win | 19.3186 |
| net_avg_loss | -30.3881 |
| avg_hold_time_bars | 5.8879 |
| exposure | 0.2484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
