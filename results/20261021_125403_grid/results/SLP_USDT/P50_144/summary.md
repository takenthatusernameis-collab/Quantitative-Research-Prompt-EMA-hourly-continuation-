# EMA Hourly Continuation — SLP/USDT P50_144

**Symbol:** SLP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.8838 |
| net_win_rate | 0.5320 |
| gross_profit_factor | 1.1315 |
| gross_win_rate | 0.5320 |
| sharpe_ratio | -0.7639 |
| sortino_ratio | -0.2221 |
| max_drawdown | 0.2746 |
| cagr | -0.1004 |
| net_avg_win | 82.1660 |
| net_avg_loss | -105.6916 |
| avg_hold_time_bars | 15.5739 |
| exposure | 0.2874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
