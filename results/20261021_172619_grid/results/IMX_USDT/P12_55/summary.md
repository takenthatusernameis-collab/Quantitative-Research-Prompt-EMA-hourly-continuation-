# EMA Hourly Continuation — IMX/USDT P12_55

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.8631 |
| net_win_rate | 0.5192 |
| gross_profit_factor | 1.0637 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | -1.0389 |
| sortino_ratio | -0.3734 |
| max_drawdown | 0.4101 |
| cagr | -0.1614 |
| net_avg_win | 69.5614 |
| net_avg_loss | -87.0206 |
| avg_hold_time_bars | 12.5958 |
| exposure | 0.3568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
