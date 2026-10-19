# EMA Hourly Continuation — KAS/USDT P26_144

**Symbol:** KAS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.5712 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -3.7313 |
| sortino_ratio | -1.2614 |
| max_drawdown | 0.7925 |
| cagr | -0.4579 |
| net_avg_win | 37.3569 |
| net_avg_loss | -60.4316 |
| avg_hold_time_bars | 14.9108 |
| exposure | 0.3951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
