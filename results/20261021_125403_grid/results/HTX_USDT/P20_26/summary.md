# EMA Hourly Continuation — HTX/USDT P20_26

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.2949 |
| net_win_rate | 0.3353 |
| gross_profit_factor | 0.5955 |
| gross_win_rate | 0.3383 |
| sharpe_ratio | -7.3774 |
| sortino_ratio | -2.0006 |
| max_drawdown | 0.9111 |
| cagr | -0.6156 |
| net_avg_win | 33.6993 |
| net_avg_loss | -57.6401 |
| avg_hold_time_bars | 5.2136 |
| exposure | 0.0795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
