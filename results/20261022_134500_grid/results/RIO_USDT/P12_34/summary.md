# EMA Hourly Continuation — RIO/USDT P12_34

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1408 |
| net_profit_factor | 0.5191 |
| net_win_rate | 0.4077 |
| gross_profit_factor | 0.7943 |
| gross_win_rate | 0.4141 |
| sharpe_ratio | -9.5047 |
| sortino_ratio | -4.9979 |
| max_drawdown | 0.9980 |
| cagr | -0.9172 |
| net_avg_win | 18.7675 |
| net_avg_loss | -24.8826 |
| avg_hold_time_bars | 3.8793 |
| exposure | 0.2508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
