# EMA Hourly Continuation — ONE/USDT P100_144

**Symbol:** ONE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.5036 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -5.0832 |
| sortino_ratio | -1.6302 |
| max_drawdown | 0.8691 |
| cagr | -0.5452 |
| net_avg_win | 38.3417 |
| net_avg_loss | -60.2750 |
| avg_hold_time_bars | 4.1957 |
| exposure | 0.0984 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
