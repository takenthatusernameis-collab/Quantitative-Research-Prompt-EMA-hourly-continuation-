# EMA Hourly Continuation — ARB/USDT P26_89

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.8784 |
| net_win_rate | 0.5300 |
| gross_profit_factor | 1.1161 |
| gross_win_rate | 0.5300 |
| sharpe_ratio | -0.7874 |
| sortino_ratio | -0.2367 |
| max_drawdown | 0.3596 |
| cagr | -0.1064 |
| net_avg_win | 77.3402 |
| net_avg_loss | -99.2635 |
| avg_hold_time_bars | 15.2995 |
| exposure | 0.3018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
