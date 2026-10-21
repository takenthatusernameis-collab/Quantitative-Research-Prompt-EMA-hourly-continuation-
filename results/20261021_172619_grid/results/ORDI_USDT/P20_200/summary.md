# EMA Hourly Continuation — ORDI/USDT P20_200

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7486 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8757 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -1.7717 |
| sortino_ratio | -0.4725 |
| max_drawdown | 0.4553 |
| cagr | -0.1958 |
| net_avg_win | 76.5260 |
| net_avg_loss | -88.7024 |
| avg_hold_time_bars | 35.2833 |
| exposure | 0.5661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
