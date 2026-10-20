# EMA Hourly Continuation — TRB/USDT P20_26

**Symbol:** TRB/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1346 |
| net_profit_factor | 0.2322 |
| net_win_rate | 0.3039 |
| gross_profit_factor | 0.6625 |
| gross_win_rate | 0.3618 |
| sharpe_ratio | -16.9999 |
| sortino_ratio | -9.1161 |
| max_drawdown | 1.0000 |
| cagr | -0.9923 |
| net_avg_win | 7.3954 |
| net_avg_loss | -13.9004 |
| avg_hold_time_bars | 1.9718 |
| exposure | 0.1201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
