# EMA Hourly Continuation — JST/USDT P50_144

**Symbol:** JST/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.4148 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.9906 |
| gross_win_rate | 0.5081 |
| sharpe_ratio | -4.9096 |
| sortino_ratio | -1.4216 |
| max_drawdown | 0.8401 |
| cagr | -0.5151 |
| net_avg_win | 30.4877 |
| net_avg_loss | -60.7374 |
| avg_hold_time_bars | 15.5035 |
| exposure | 0.3024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
