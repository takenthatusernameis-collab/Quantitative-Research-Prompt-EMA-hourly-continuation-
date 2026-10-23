# EMA Hourly Continuation — ACE/USDT P20_21

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 933 |
| net_profit_factor | 0.2057 |
| net_win_rate | 0.3558 |
| gross_profit_factor | 0.9140 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -12.6059 |
| sortino_ratio | -5.5909 |
| max_drawdown | 0.9995 |
| cagr | -0.9511 |
| net_avg_win | 7.7958 |
| net_avg_loss | -20.9372 |
| avg_hold_time_bars | 2.8660 |
| exposure | 0.1210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
