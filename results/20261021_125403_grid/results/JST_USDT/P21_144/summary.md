# EMA Hourly Continuation — JST/USDT P21_144

**Symbol:** JST/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.7145 |
| net_win_rate | 0.5182 |
| gross_profit_factor | 1.0904 |
| gross_win_rate | 0.5266 |
| sharpe_ratio | -1.8055 |
| sortino_ratio | -0.4855 |
| max_drawdown | 0.4724 |
| cagr | -0.2031 |
| net_avg_win | 58.9694 |
| net_avg_loss | -88.7752 |
| avg_hold_time_bars | 32.6555 |
| exposure | 0.5275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
