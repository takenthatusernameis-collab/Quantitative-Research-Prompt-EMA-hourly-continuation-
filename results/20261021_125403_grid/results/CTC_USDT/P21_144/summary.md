# EMA Hourly Continuation — CTC/USDT P21_144

**Symbol:** CTC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.8587 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.0840 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -0.9303 |
| sortino_ratio | -0.2765 |
| max_drawdown | 0.4082 |
| cagr | -0.1229 |
| net_avg_win | 76.1037 |
| net_avg_loss | -97.3210 |
| avg_hold_time_bars | 25.8061 |
| exposure | 0.5020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
