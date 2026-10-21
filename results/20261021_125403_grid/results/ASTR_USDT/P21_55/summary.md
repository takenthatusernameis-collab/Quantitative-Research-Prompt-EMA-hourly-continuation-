# EMA Hourly Continuation — ASTR/USDT P21_55

**Symbol:** ASTR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.7031 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -2.7230 |
| sortino_ratio | -0.9270 |
| max_drawdown | 0.6675 |
| cagr | -0.3472 |
| net_avg_win | 54.5559 |
| net_avg_loss | -78.9783 |
| avg_hold_time_bars | 8.2222 |
| exposure | 0.2110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
