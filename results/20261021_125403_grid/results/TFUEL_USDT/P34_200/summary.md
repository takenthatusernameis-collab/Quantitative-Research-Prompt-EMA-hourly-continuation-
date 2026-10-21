# EMA Hourly Continuation — TFUEL/USDT P34_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.5871 |
| net_win_rate | 0.4198 |
| gross_profit_factor | 0.7332 |
| gross_win_rate | 0.4198 |
| sharpe_ratio | -3.3569 |
| sortino_ratio | -0.9140 |
| max_drawdown | 0.6640 |
| cagr | -0.3449 |
| net_avg_win | 59.4013 |
| net_avg_loss | -73.2038 |
| avg_hold_time_bars | 26.2246 |
| exposure | 0.4438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
