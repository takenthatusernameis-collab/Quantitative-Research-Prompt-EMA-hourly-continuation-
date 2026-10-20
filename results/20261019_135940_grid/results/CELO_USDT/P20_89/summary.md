# EMA Hourly Continuation — CELO/USDT P20_89

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.6973 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 1.0251 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -3.0433 |
| sortino_ratio | -1.0825 |
| max_drawdown | 0.7411 |
| cagr | -0.4010 |
| net_avg_win | 53.2302 |
| net_avg_loss | -74.4393 |
| avg_hold_time_bars | 14.6541 |
| exposure | 0.4217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
