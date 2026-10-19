# EMA Hourly Continuation — VET/USDT P12_100

**Symbol:** VET/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.6854 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0729 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -3.5719 |
| sortino_ratio | -1.3307 |
| max_drawdown | 0.8155 |
| cagr | -0.4742 |
| net_avg_win | 49.4270 |
| net_avg_loss | -72.1173 |
| avg_hold_time_bars | 17.6657 |
| exposure | 0.5669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
