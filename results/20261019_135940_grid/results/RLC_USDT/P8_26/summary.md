# EMA Hourly Continuation — RLC/USDT P8_26

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1466 |
| net_profit_factor | 0.4935 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.9273 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -8.9265 |
| sortino_ratio | -4.8117 |
| max_drawdown | 0.9974 |
| cagr | -0.9043 |
| net_avg_win | 14.7009 |
| net_avg_loss | -24.4592 |
| avg_hold_time_bars | 4.4905 |
| exposure | 0.2992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
