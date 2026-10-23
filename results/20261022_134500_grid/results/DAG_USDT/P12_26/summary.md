# EMA Hourly Continuation — DAG/USDT P12_26

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1420 |
| net_profit_factor | 0.3738 |
| net_win_rate | 0.3606 |
| gross_profit_factor | 0.6874 |
| gross_win_rate | 0.3775 |
| sharpe_ratio | -14.1090 |
| sortino_ratio | -7.5257 |
| max_drawdown | 1.0000 |
| cagr | -0.9815 |
| net_avg_win | 11.6600 |
| net_avg_loss | -17.5875 |
| avg_hold_time_bars | 2.5859 |
| exposure | 0.1669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
