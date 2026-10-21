# EMA Hourly Continuation — TRB/USDT P8_34

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.7144 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9290 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -3.3986 |
| sortino_ratio | -1.3065 |
| max_drawdown | 0.7889 |
| cagr | -0.4509 |
| net_avg_win | 56.8541 |
| net_avg_loss | -70.5330 |
| avg_hold_time_bars | 9.2863 |
| exposure | 0.3068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
