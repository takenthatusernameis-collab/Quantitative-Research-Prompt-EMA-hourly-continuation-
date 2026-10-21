# EMA Hourly Continuation — MNT/USDT P12_34

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.6899 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 1.0241 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -3.3683 |
| sortino_ratio | -1.1966 |
| max_drawdown | 0.7744 |
| cagr | -0.4220 |
| net_avg_win | 54.8885 |
| net_avg_loss | -77.7652 |
| avg_hold_time_bars | 8.3540 |
| exposure | 0.2328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
