# EMA Hourly Continuation — BIGTIME/USDT P8_26

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1411 |
| net_profit_factor | 0.5310 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.9073 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -8.5825 |
| sortino_ratio | -4.5352 |
| max_drawdown | 0.9961 |
| cagr | -0.8887 |
| net_avg_win | 18.0153 |
| net_avg_loss | -27.0551 |
| avg_hold_time_bars | 4.4493 |
| exposure | 0.2841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
