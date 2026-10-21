# EMA Hourly Continuation — PYTH/USDT P34_55

**Symbol:** PYTH/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.6850 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.8941 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -2.2580 |
| sortino_ratio | -0.5595 |
| max_drawdown | 0.5101 |
| cagr | -0.2268 |
| net_avg_win | 73.9019 |
| net_avg_loss | -93.2388 |
| avg_hold_time_bars | 6.2351 |
| exposure | 0.0856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
