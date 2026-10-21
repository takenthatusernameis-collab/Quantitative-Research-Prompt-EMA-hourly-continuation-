# EMA Hourly Continuation — ZK/USDT P89_144

**Symbol:** ZK/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.7105 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9109 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -1.9329 |
| sortino_ratio | -0.4865 |
| max_drawdown | 0.4183 |
| cagr | -0.2006 |
| net_avg_win | 72.5341 |
| net_avg_loss | -92.6896 |
| avg_hold_time_bars | 9.0897 |
| exposure | 0.1285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
