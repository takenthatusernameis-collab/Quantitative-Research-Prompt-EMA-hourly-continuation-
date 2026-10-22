# EMA Hourly Continuation — IOTA/USDT P55_89

**Symbol:** IOTA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.4400 |
| net_win_rate | 0.4335 |
| gross_profit_factor | 0.8496 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -6.6239 |
| sortino_ratio | -2.4259 |
| max_drawdown | 0.9511 |
| cagr | -0.6926 |
| net_avg_win | 25.6894 |
| net_avg_loss | -44.6785 |
| avg_hold_time_bars | 4.0792 |
| exposure | 0.1240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
