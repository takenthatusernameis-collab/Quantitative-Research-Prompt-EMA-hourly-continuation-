# EMA Hourly Continuation — AERO/USDT P12_200

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 1.1454 |
| net_win_rate | 0.5650 |
| gross_profit_factor | 1.2709 |
| gross_win_rate | 0.5650 |
| sharpe_ratio | 0.7536 |
| sortino_ratio | 0.1725 |
| max_drawdown | 0.1400 |
| cagr | 0.0720 |
| net_avg_win | 108.0706 |
| net_avg_loss | -122.5735 |
| avg_hold_time_bars | 68.2154 |
| exposure | 0.7628 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
