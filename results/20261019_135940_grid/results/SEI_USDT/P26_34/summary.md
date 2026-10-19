# EMA Hourly Continuation — SEI/USDT P26_34

**Symbol:** SEI/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1068 |
| net_profit_factor | 0.3120 |
| net_win_rate | 0.3942 |
| gross_profit_factor | 0.6731 |
| gross_win_rate | 0.4242 |
| sharpe_ratio | -12.0293 |
| sortino_ratio | -5.6176 |
| max_drawdown | 0.9994 |
| cagr | -0.9478 |
| net_avg_win | 10.7653 |
| net_avg_loss | -22.4516 |
| avg_hold_time_bars | 1.9831 |
| exposure | 0.0963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
