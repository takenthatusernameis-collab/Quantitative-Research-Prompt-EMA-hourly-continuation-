# EMA Hourly Continuation — ELON/USDT P20_34

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1042 |
| net_profit_factor | 0.3185 |
| net_win_rate | 0.3973 |
| gross_profit_factor | 0.6969 |
| gross_win_rate | 0.4040 |
| sharpe_ratio | -11.0902 |
| sortino_ratio | -5.1529 |
| max_drawdown | 0.9984 |
| cagr | -0.9233 |
| net_avg_win | 11.2693 |
| net_avg_loss | -23.3275 |
| avg_hold_time_bars | 2.8464 |
| exposure | 0.1348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
