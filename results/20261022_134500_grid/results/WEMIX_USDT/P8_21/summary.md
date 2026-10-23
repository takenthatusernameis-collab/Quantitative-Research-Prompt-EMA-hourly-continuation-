# EMA Hourly Continuation — WEMIX/USDT P8_21

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2187 |
| net_profit_factor | 0.1577 |
| net_win_rate | 0.2670 |
| gross_profit_factor | 0.3894 |
| gross_win_rate | 0.2963 |
| sharpe_ratio | -23.5667 |
| sortino_ratio | -16.0438 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 3.2071 |
| net_avg_loss | -7.4067 |
| avg_hold_time_bars | 2.7755 |
| exposure | 0.2759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
