# EMA Hourly Continuation — ACE/USDT P8_100

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.7512 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -1.8833 |
| sortino_ratio | -0.5459 |
| max_drawdown | 0.4996 |
| cagr | -0.2220 |
| net_avg_win | 70.4515 |
| net_avg_loss | -87.2752 |
| avg_hold_time_bars | 35.1175 |
| exposure | 0.6627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
