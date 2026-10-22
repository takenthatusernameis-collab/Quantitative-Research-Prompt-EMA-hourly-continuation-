# EMA Hourly Continuation — CYBER/USDT P34_144

**Symbol:** CYBER/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.8229 |
| net_win_rate | 0.5088 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -1.1568 |
| sortino_ratio | -0.3306 |
| max_drawdown | 0.3831 |
| cagr | -0.1427 |
| net_avg_win | 73.7794 |
| net_avg_loss | -92.8775 |
| avg_hold_time_bars | 21.2191 |
| exposure | 0.3829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
