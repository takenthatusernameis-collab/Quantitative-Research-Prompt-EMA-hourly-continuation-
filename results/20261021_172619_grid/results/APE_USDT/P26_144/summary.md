# EMA Hourly Continuation — APE/USDT P26_144

**Symbol:** APE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.8360 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0078 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -0.9082 |
| sortino_ratio | -0.2315 |
| max_drawdown | 0.2961 |
| cagr | -0.1029 |
| net_avg_win | 76.0007 |
| net_avg_loss | -93.2458 |
| avg_hold_time_bars | 35.3544 |
| exposure | 0.5078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
