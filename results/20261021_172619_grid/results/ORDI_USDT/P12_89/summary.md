# EMA Hourly Continuation — ORDI/USDT P12_89

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.7339 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8774 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -2.5233 |
| sortino_ratio | -0.8252 |
| max_drawdown | 0.6269 |
| cagr | -0.3160 |
| net_avg_win | 69.4864 |
| net_avg_loss | -80.4954 |
| avg_hold_time_bars | 20.8927 |
| exposure | 0.5043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
