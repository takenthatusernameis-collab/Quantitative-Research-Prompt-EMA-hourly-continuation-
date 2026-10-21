# EMA Hourly Continuation — POKT/USDT P12_34

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.5795 |
| net_win_rate | 0.3994 |
| gross_profit_factor | 0.7609 |
| gross_win_rate | 0.4009 |
| sharpe_ratio | -5.3676 |
| sortino_ratio | -1.9227 |
| max_drawdown | 0.8953 |
| cagr | -0.5899 |
| net_avg_win | 47.7739 |
| net_avg_loss | -54.8188 |
| avg_hold_time_bars | 6.8731 |
| exposure | 0.2009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
