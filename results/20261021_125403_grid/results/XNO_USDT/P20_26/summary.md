# EMA Hourly Continuation — XNO/USDT P20_26

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.4315 |
| net_win_rate | 0.3619 |
| gross_profit_factor | 0.6204 |
| gross_win_rate | 0.3619 |
| sharpe_ratio | -4.0215 |
| sortino_ratio | -0.8281 |
| max_drawdown | 0.6316 |
| cagr | -0.3196 |
| net_avg_win | 61.8928 |
| net_avg_loss | -81.3515 |
| avg_hold_time_bars | 4.3286 |
| exposure | 0.0413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
