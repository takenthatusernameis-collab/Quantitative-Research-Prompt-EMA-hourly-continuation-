# EMA Hourly Continuation — CRV/USDT P55_89

**Symbol:** CRV/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.8275 |
| net_win_rate | 0.5273 |
| gross_profit_factor | 1.1086 |
| gross_win_rate | 0.5273 |
| sharpe_ratio | -1.0293 |
| sortino_ratio | -0.2620 |
| max_drawdown | 0.2907 |
| cagr | -0.1141 |
| net_avg_win | 76.7575 |
| net_avg_loss | -103.4815 |
| avg_hold_time_bars | 5.7846 |
| exposure | 0.0818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
