# EMA Hourly Continuation — XDC/USDT P89_144

**Symbol:** XDC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.5975 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9180 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -2.1992 |
| sortino_ratio | -0.5004 |
| max_drawdown | 0.4616 |
| cagr | -0.2050 |
| net_avg_win | 52.4155 |
| net_avg_loss | -85.6555 |
| avg_hold_time_bars | 7.9602 |
| exposure | 0.0908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
