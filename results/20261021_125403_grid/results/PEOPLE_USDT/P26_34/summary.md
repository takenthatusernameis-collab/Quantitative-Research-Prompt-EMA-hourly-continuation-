# EMA Hourly Continuation — PEOPLE/USDT P26_34

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.8304 |
| net_win_rate | 0.5407 |
| gross_profit_factor | 1.1730 |
| gross_win_rate | 0.5407 |
| sharpe_ratio | -0.9145 |
| sortino_ratio | -0.2074 |
| max_drawdown | 0.2824 |
| cagr | -0.0909 |
| net_avg_win | 78.6399 |
| net_avg_loss | -111.4638 |
| avg_hold_time_bars | 4.5000 |
| exposure | 0.0501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
