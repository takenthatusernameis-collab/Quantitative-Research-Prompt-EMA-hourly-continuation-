# EMA Hourly Continuation — DBR/USDT P34_200

**Symbol:** DBR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -1.9437 |
| sortino_ratio | -0.4682 |
| max_drawdown | 0.3817 |
| cagr | -0.1938 |
| net_avg_win | 69.6410 |
| net_avg_loss | -92.5187 |
| avg_hold_time_bars | 35.9956 |
| exposure | 0.4688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
