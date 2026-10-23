# EMA Hourly Continuation — GLM/USDT P89_144

**Symbol:** GLM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.4521 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8691 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -5.2800 |
| sortino_ratio | -1.6876 |
| max_drawdown | 0.8722 |
| cagr | -0.5554 |
| net_avg_win | 31.8776 |
| net_avg_loss | -56.6660 |
| avg_hold_time_bars | 6.0020 |
| exposure | 0.1378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
