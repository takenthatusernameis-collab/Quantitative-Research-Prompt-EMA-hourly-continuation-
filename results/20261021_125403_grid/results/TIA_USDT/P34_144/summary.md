# EMA Hourly Continuation — TIA/USDT P34_144

**Symbol:** TIA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7959 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9290 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -1.2832 |
| sortino_ratio | -0.3308 |
| max_drawdown | 0.3378 |
| cagr | -0.1424 |
| net_avg_win | 78.9804 |
| net_avg_loss | -92.7777 |
| avg_hold_time_bars | 27.8196 |
| exposure | 0.4135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
