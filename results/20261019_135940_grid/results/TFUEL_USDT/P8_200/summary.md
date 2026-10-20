# EMA Hourly Continuation — TFUEL/USDT P8_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5053 |
| net_win_rate | 0.4003 |
| gross_profit_factor | 0.7341 |
| gross_win_rate | 0.4170 |
| sharpe_ratio | -5.9599 |
| sortino_ratio | -2.1443 |
| max_drawdown | 0.9274 |
| cagr | -0.6413 |
| net_avg_win | 35.9206 |
| net_avg_loss | -47.4475 |
| avg_hold_time_bars | 23.8858 |
| exposure | 0.7101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
