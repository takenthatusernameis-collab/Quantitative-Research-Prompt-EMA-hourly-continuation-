# EMA Hourly Continuation — AVA/USDT P55_89

**Symbol:** AVA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7531 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0515 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -1.6308 |
| sortino_ratio | -0.4325 |
| max_drawdown | 0.4103 |
| cagr | -0.1794 |
| net_avg_win | 68.6062 |
| net_avg_loss | -96.0713 |
| avg_hold_time_bars | 6.3333 |
| exposure | 0.0976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
