# EMA Hourly Continuation — TRAC/USDT P12_21

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1143 |
| net_profit_factor | 0.3798 |
| net_win_rate | 0.3911 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4234 |
| sharpe_ratio | -11.4981 |
| sortino_ratio | -5.4891 |
| max_drawdown | 0.9993 |
| cagr | -0.9428 |
| net_avg_win | 13.6916 |
| net_avg_loss | -23.1503 |
| avg_hold_time_bars | 3.6815 |
| exposure | 0.1913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
