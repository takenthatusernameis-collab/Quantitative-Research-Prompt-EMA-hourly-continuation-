# EMA Hourly Continuation — XTZ/USDT P26_144

**Symbol:** XTZ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7346 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.1191 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -2.2229 |
| sortino_ratio | -0.6879 |
| max_drawdown | 0.5750 |
| cagr | -0.2759 |
| net_avg_win | 63.0039 |
| net_avg_loss | -90.2039 |
| avg_hold_time_bars | 23.3739 |
| exposure | 0.5057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
