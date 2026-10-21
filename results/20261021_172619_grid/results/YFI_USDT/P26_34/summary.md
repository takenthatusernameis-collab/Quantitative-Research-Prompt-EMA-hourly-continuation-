# EMA Hourly Continuation — YFI/USDT P26_34

**Symbol:** YFI/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.5303 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -3.1995 |
| sortino_ratio | -0.7838 |
| max_drawdown | 0.6048 |
| cagr | -0.3005 |
| net_avg_win | 47.9109 |
| net_avg_loss | -85.4578 |
| avg_hold_time_bars | 4.7604 |
| exposure | 0.0620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
