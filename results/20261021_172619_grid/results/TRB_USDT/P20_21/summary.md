# EMA Hourly Continuation — TRB/USDT P20_21

**Symbol:** TRB/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 158 |
| net_profit_factor | 0.4506 |
| net_win_rate | 0.3797 |
| gross_profit_factor | 0.6469 |
| gross_win_rate | 0.3797 |
| sharpe_ratio | -3.3003 |
| sortino_ratio | -0.5903 |
| max_drawdown | 0.5128 |
| cagr | -0.2409 |
| net_avg_win | 68.4839 |
| net_avg_loss | -93.0587 |
| avg_hold_time_bars | 4.3924 |
| exposure | 0.0314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
