# EMA Hourly Continuation — KCS/USDT P50_55

**Symbol:** KCS/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 842 |
| net_profit_factor | 0.0669 |
| net_win_rate | 0.1853 |
| gross_profit_factor | 0.6160 |
| gross_win_rate | 0.3314 |
| sharpe_ratio | -18.3817 |
| sortino_ratio | -9.0725 |
| max_drawdown | 1.0000 |
| cagr | -0.9939 |
| net_avg_win | 4.5954 |
| net_avg_loss | -15.6222 |
| avg_hold_time_bars | 2.1734 |
| exposure | 0.0832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
