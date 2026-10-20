# EMA Hourly Continuation — FIDA/USDT P12_55

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 942 |
| net_profit_factor | 0.5429 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8806 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -5.7647 |
| sortino_ratio | -2.4819 |
| max_drawdown | 0.9531 |
| cagr | -0.6988 |
| net_avg_win | 26.1582 |
| net_avg_loss | -40.8154 |
| avg_hold_time_bars | 10.1348 |
| exposure | 0.4320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
