# EMA Hourly Continuation — MOVR/USDT P12_100

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.5822 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8678 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -4.7816 |
| sortino_ratio | -1.7712 |
| max_drawdown | 0.8836 |
| cagr | -0.5700 |
| net_avg_win | 39.4317 |
| net_avg_loss | -54.7080 |
| avg_hold_time_bars | 18.6466 |
| exposure | 0.5899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
