# EMA Hourly Continuation — ONE/USDT P20_144

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.6836 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -3.0879 |
| sortino_ratio | -0.9131 |
| max_drawdown | 0.7044 |
| cagr | -0.3598 |
| net_avg_win | 69.3049 |
| net_avg_loss | -88.3471 |
| avg_hold_time_bars | 28.9379 |
| exposure | 0.5932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
