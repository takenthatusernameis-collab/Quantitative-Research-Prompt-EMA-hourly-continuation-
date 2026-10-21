# EMA Hourly Continuation — YFI/USDT P55_200

**Symbol:** YFI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7722 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0418 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -1.4896 |
| sortino_ratio | -0.3928 |
| max_drawdown | 0.4029 |
| cagr | -0.1651 |
| net_avg_win | 71.6374 |
| net_avg_loss | -96.6832 |
| avg_hold_time_bars | 25.5664 |
| exposure | 0.3922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
