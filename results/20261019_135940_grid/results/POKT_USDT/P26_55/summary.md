# EMA Hourly Continuation — POKT/USDT P26_55

**Symbol:** POKT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.4669 |
| net_win_rate | 0.3971 |
| gross_profit_factor | 0.8682 |
| gross_win_rate | 0.4117 |
| sharpe_ratio | -9.1723 |
| sortino_ratio | -4.1375 |
| max_drawdown | 0.9945 |
| cagr | -0.8708 |
| net_avg_win | 21.2883 |
| net_avg_loss | -30.0315 |
| avg_hold_time_bars | 4.7631 |
| exposure | 0.2220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
