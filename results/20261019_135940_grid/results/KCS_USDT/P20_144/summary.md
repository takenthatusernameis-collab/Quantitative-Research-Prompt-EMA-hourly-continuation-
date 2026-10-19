# EMA Hourly Continuation — KCS/USDT P20_144

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.3991 |
| net_win_rate | 0.4143 |
| gross_profit_factor | 0.8859 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -6.7932 |
| sortino_ratio | -2.1788 |
| max_drawdown | 0.9408 |
| cagr | -0.6719 |
| net_avg_win | 29.0149 |
| net_avg_loss | -51.4125 |
| avg_hold_time_bars | 22.3796 |
| exposure | 0.5280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
