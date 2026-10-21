# EMA Hourly Continuation — TRX/USDT P8_12

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 188 |
| net_profit_factor | 0.4562 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.2136 |
| gross_win_rate | 0.5372 |
| sharpe_ratio | -3.3771 |
| sortino_ratio | -0.6813 |
| max_drawdown | 0.5466 |
| cagr | -0.2687 |
| net_avg_win | 48.5640 |
| net_avg_loss | -106.4583 |
| avg_hold_time_bars | 6.8351 |
| exposure | 0.0584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
