# EMA Hourly Continuation — SHR/USDT P12_55

**Symbol:** SHR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1330 |
| net_profit_factor | 0.4508 |
| net_win_rate | 0.3459 |
| gross_profit_factor | 0.6923 |
| gross_win_rate | 0.3489 |
| sharpe_ratio | -10.8367 |
| sortino_ratio | -5.4990 |
| max_drawdown | 0.9989 |
| cagr | -0.9311 |
| net_avg_win | 17.8199 |
| net_avg_loss | -20.9028 |
| avg_hold_time_bars | 5.8865 |
| exposure | 0.3543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
