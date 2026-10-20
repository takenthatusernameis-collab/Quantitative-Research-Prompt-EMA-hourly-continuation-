# EMA Hourly Continuation — EUL/USDT P34_89

**Symbol:** EUL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.3945 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.6046 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -5.7320 |
| sortino_ratio | -2.0142 |
| max_drawdown | 0.9161 |
| cagr | -0.6231 |
| net_avg_win | 22.8956 |
| net_avg_loss | -41.1181 |
| avg_hold_time_bars | 8.4115 |
| exposure | 0.2397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
