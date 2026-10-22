# EMA Hourly Continuation — DIA/USDT P20_26

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.6343 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9819 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.4115 |
| sortino_ratio | -0.6034 |
| max_drawdown | 0.5267 |
| cagr | -0.2407 |
| net_avg_win | 57.1305 |
| net_avg_loss | -90.0686 |
| avg_hold_time_bars | 4.3783 |
| exposure | 0.0602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
