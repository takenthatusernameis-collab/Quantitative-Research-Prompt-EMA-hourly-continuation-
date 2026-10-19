# EMA Hourly Continuation — KAS/USDT P89_144

**Symbol:** KAS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.3629 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.7204 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -5.9150 |
| sortino_ratio | -1.8690 |
| max_drawdown | 0.9119 |
| cagr | -0.6116 |
| net_avg_win | 23.5912 |
| net_avg_loss | -49.4309 |
| avg_hold_time_bars | 4.7732 |
| exposure | 0.1100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
