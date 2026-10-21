# EMA Hourly Continuation — XMR/USDT P21_34

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 179 |
| net_profit_factor | 0.4894 |
| net_win_rate | 0.4134 |
| gross_profit_factor | 0.6996 |
| gross_win_rate | 0.4134 |
| sharpe_ratio | -2.9035 |
| sortino_ratio | -0.5517 |
| max_drawdown | 0.4786 |
| cagr | -0.2242 |
| net_avg_win | 61.0656 |
| net_avg_loss | -87.9348 |
| avg_hold_time_bars | 4.4022 |
| exposure | 0.0358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
