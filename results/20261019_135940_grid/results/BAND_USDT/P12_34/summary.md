# EMA Hourly Continuation — BAND/USDT P12_34

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1117 |
| net_profit_factor | 0.4924 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.9412 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -7.7476 |
| sortino_ratio | -3.6402 |
| max_drawdown | 0.9892 |
| cagr | -0.8314 |
| net_avg_win | 19.1423 |
| net_avg_loss | -31.6205 |
| avg_hold_time_bars | 5.3957 |
| exposure | 0.2727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
