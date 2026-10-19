# EMA Hourly Continuation — XTZ/USDT P89_144

**Symbol:** XTZ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.5323 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 1.0737 |
| gross_win_rate | 0.5247 |
| sharpe_ratio | -4.0541 |
| sortino_ratio | -1.2928 |
| max_drawdown | 0.7912 |
| cagr | -0.4624 |
| net_avg_win | 35.6656 |
| net_avg_loss | -66.2095 |
| avg_hold_time_bars | 5.2170 |
| exposure | 0.1202 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
