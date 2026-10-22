# EMA Hourly Continuation — BOSON/USDT P21_144

**Symbol:** BOSON/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.7775 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 1.0118 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -2.0941 |
| sortino_ratio | -0.6856 |
| max_drawdown | 0.5544 |
| cagr | -0.2749 |
| net_avg_win | 74.1610 |
| net_avg_loss | -90.5289 |
| avg_hold_time_bars | 19.9422 |
| exposure | 0.4859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
