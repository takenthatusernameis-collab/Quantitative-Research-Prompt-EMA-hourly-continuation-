# EMA Hourly Continuation — FLUX/USDT P144_200

**Symbol:** FLUX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 192 |
| net_profit_factor | 0.6953 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9383 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.4795 |
| sortino_ratio | -0.2938 |
| max_drawdown | 0.3274 |
| cagr | -0.1260 |
| net_avg_win | 69.6630 |
| net_avg_loss | -96.0985 |
| avg_hold_time_bars | 7.7917 |
| exposure | 0.0680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
