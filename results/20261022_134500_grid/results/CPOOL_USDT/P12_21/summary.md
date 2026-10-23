# EMA Hourly Continuation — CPOOL/USDT P12_21

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1463 |
| net_profit_factor | 0.5013 |
| net_win_rate | 0.4163 |
| gross_profit_factor | 0.8518 |
| gross_win_rate | 0.4327 |
| sharpe_ratio | -11.2618 |
| sortino_ratio | -6.0560 |
| max_drawdown | 0.9996 |
| cagr | -0.9537 |
| net_avg_win | 16.5018 |
| net_avg_loss | -23.4721 |
| avg_hold_time_bars | 2.3732 |
| exposure | 0.1578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
