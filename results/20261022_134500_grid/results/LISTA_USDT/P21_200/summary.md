# EMA Hourly Continuation — LISTA/USDT P21_200

**Symbol:** LISTA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6480 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8655 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -2.7915 |
| sortino_ratio | -0.8327 |
| max_drawdown | 0.6048 |
| cagr | -0.3205 |
| net_avg_win | 57.8821 |
| net_avg_loss | -75.3665 |
| avg_hold_time_bars | 27.9177 |
| exposure | 0.5638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
