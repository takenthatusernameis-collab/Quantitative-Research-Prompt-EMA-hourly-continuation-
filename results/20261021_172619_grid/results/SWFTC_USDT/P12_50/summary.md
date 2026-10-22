# EMA Hourly Continuation — SWFTC/USDT P12_50

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.7117 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9121 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -2.5115 |
| sortino_ratio | -0.8578 |
| max_drawdown | 0.6392 |
| cagr | -0.3250 |
| net_avg_win | 56.5263 |
| net_avg_loss | -72.7801 |
| avg_hold_time_bars | 10.9075 |
| exposure | 0.2841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
