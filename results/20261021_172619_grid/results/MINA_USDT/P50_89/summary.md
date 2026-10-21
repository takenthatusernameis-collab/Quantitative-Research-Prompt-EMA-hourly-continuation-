# EMA Hourly Continuation — MINA/USDT P50_89

**Symbol:** MINA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7473 |
| net_win_rate | 0.5110 |
| gross_profit_factor | 1.0348 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -1.8200 |
| sortino_ratio | -0.5288 |
| max_drawdown | 0.5127 |
| cagr | -0.2156 |
| net_avg_win | 64.6051 |
| net_avg_loss | -90.3365 |
| avg_hold_time_bars | 6.9511 |
| exposure | 0.1292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
