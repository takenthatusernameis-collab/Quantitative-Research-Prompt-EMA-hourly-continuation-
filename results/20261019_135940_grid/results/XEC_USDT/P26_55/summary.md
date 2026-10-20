# EMA Hourly Continuation — XEC/USDT P26_55

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 994 |
| net_profit_factor | 0.4859 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 1.0021 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -7.8866 |
| sortino_ratio | -3.5136 |
| max_drawdown | 0.9874 |
| cagr | -0.8226 |
| net_avg_win | 20.7330 |
| net_avg_loss | -35.2983 |
| avg_hold_time_bars | 4.6891 |
| exposure | 0.2109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
