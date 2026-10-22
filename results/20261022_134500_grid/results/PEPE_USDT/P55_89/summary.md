# EMA Hourly Continuation — PEPE/USDT P55_89

**Symbol:** PEPE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.5023 |
| net_win_rate | 0.4203 |
| gross_profit_factor | 0.8381 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -7.2036 |
| sortino_ratio | -2.7135 |
| max_drawdown | 0.9665 |
| cagr | -0.7401 |
| net_avg_win | 32.7120 |
| net_avg_loss | -47.2235 |
| avg_hold_time_bars | 3.5458 |
| exposure | 0.1143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
