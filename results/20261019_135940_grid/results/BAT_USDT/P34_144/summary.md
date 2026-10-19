# EMA Hourly Continuation — BAT/USDT P34_144

**Symbol:** BAT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.5556 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8542 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -3.9694 |
| sortino_ratio | -1.2425 |
| max_drawdown | 0.7889 |
| cagr | -0.4565 |
| net_avg_win | 42.6023 |
| net_avg_loss | -64.6010 |
| avg_hold_time_bars | 17.0994 |
| exposure | 0.3910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
