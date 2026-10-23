# EMA Hourly Continuation — TRB/USDT P12_50

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1113 |
| net_profit_factor | 0.4939 |
| net_win_rate | 0.4322 |
| gross_profit_factor | 0.8326 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -7.9930 |
| sortino_ratio | -3.7452 |
| max_drawdown | 0.9899 |
| cagr | -0.8386 |
| net_avg_win | 20.0857 |
| net_avg_loss | -30.9505 |
| avg_hold_time_bars | 6.9964 |
| exposure | 0.3524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
