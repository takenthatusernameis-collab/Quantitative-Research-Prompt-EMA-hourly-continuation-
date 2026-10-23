# EMA Hourly Continuation — MEW/USDT P26_89

**Symbol:** MEW/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.5558 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8332 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -4.7697 |
| sortino_ratio | -1.7939 |
| max_drawdown | 0.8872 |
| cagr | -0.5758 |
| net_avg_win | 33.7160 |
| net_avg_loss | -51.1528 |
| avg_hold_time_bars | 8.9233 |
| exposure | 0.2908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
