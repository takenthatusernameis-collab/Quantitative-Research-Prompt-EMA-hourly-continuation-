# EMA Hourly Continuation — CELO/USDT P12_26

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6746 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9577 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -3.0879 |
| sortino_ratio | -1.0507 |
| max_drawdown | 0.7062 |
| cagr | -0.3816 |
| net_avg_win | 52.9730 |
| net_avg_loss | -74.2033 |
| avg_hold_time_bars | 5.6025 |
| exposure | 0.1435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
