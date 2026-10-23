# EMA Hourly Continuation — ALPINE/USDT P20_89

**Symbol:** ALPINE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.5027 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8042 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -6.2272 |
| sortino_ratio | -2.3682 |
| max_drawdown | 0.9474 |
| cagr | -0.6868 |
| net_avg_win | 29.8833 |
| net_avg_loss | -45.2880 |
| avg_hold_time_bars | 11.7230 |
| exposure | 0.3943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
