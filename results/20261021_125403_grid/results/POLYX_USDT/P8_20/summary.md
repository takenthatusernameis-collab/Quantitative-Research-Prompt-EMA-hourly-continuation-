# EMA Hourly Continuation — POLYX/USDT P8_20

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.6784 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 1.0088 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -4.0220 |
| sortino_ratio | -1.5118 |
| max_drawdown | 0.8367 |
| cagr | -0.4993 |
| net_avg_win | 52.5186 |
| net_avg_loss | -72.1795 |
| avg_hold_time_bars | 5.4519 |
| exposure | 0.1700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
