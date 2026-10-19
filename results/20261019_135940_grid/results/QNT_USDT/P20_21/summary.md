# EMA Hourly Continuation — QNT/USDT P20_21

**Symbol:** QNT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1302 |
| net_profit_factor | 0.0756 |
| net_win_rate | 0.2627 |
| gross_profit_factor | 0.4140 |
| gross_win_rate | 0.3564 |
| sharpe_ratio | -20.3200 |
| sortino_ratio | -11.5884 |
| max_drawdown | 1.0000 |
| cagr | -0.9986 |
| net_avg_win | 2.3909 |
| net_avg_loss | -11.2684 |
| avg_hold_time_bars | 1.6851 |
| exposure | 0.0997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
