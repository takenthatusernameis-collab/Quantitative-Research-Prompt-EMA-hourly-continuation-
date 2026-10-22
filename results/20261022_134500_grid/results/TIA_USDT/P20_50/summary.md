# EMA Hourly Continuation — TIA/USDT P20_50

**Symbol:** TIA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.6400 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 1.0121 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -5.2883 |
| sortino_ratio | -2.3602 |
| max_drawdown | 0.9437 |
| cagr | -0.6773 |
| net_avg_win | 34.8013 |
| net_avg_loss | -50.3959 |
| avg_hold_time_bars | 4.5900 |
| exposure | 0.2086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
