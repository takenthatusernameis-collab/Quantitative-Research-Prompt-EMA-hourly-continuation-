# EMA Hourly Continuation — SNX/USDT P50_55

**Symbol:** SNX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 129 |
| net_profit_factor | 0.8007 |
| net_win_rate | 0.5349 |
| gross_profit_factor | 1.1585 |
| gross_win_rate | 0.5349 |
| sharpe_ratio | -0.8039 |
| sortino_ratio | -0.1319 |
| max_drawdown | 0.2150 |
| cagr | -0.0583 |
| net_avg_win | 81.8314 |
| net_avg_loss | -117.5261 |
| avg_hold_time_bars | 5.5116 |
| exposure | 0.0322 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
