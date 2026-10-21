# EMA Hourly Continuation — ORDI/USDT P89_144

**Symbol:** ORDI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.6947 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -1.8256 |
| sortino_ratio | -0.4385 |
| max_drawdown | 0.4066 |
| cagr | -0.1826 |
| net_avg_win | 66.9859 |
| net_avg_loss | -87.9519 |
| avg_hold_time_bars | 7.1519 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
