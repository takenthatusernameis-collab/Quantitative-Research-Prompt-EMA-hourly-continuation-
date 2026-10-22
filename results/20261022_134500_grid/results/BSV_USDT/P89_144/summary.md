# EMA Hourly Continuation — BSV/USDT P89_144

**Symbol:** BSV/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.4204 |
| net_win_rate | 0.4125 |
| gross_profit_factor | 0.8023 |
| gross_win_rate | 0.4291 |
| sharpe_ratio | -6.7390 |
| sortino_ratio | -2.2227 |
| max_drawdown | 0.9391 |
| cagr | -0.6718 |
| net_avg_win | 30.4069 |
| net_avg_loss | -50.7890 |
| avg_hold_time_bars | 4.9779 |
| exposure | 0.1229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
