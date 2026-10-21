# EMA Hourly Continuation — T/USDT P50_55

**Symbol:** T/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.4936 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9525 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -3.2782 |
| sortino_ratio | -0.7676 |
| max_drawdown | 0.6013 |
| cagr | -0.3013 |
| net_avg_win | 43.9571 |
| net_avg_loss | -85.8015 |
| avg_hold_time_bars | 5.6877 |
| exposure | 0.0692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
