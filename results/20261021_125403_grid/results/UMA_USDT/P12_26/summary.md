# EMA Hourly Continuation — UMA/USDT P12_26

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6016 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.8943 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -3.9721 |
| sortino_ratio | -1.3856 |
| max_drawdown | 0.8047 |
| cagr | -0.4712 |
| net_avg_win | 42.4363 |
| net_avg_loss | -64.6226 |
| avg_hold_time_bars | 5.3956 |
| exposure | 0.1457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
