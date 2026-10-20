# EMA Hourly Continuation — XPR/USDT P55_144

**Symbol:** XPR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.3938 |
| net_win_rate | 0.4206 |
| gross_profit_factor | 0.6963 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -5.8914 |
| sortino_ratio | -1.8605 |
| max_drawdown | 0.9032 |
| cagr | -0.6041 |
| net_avg_win | 27.6514 |
| net_avg_loss | -50.9801 |
| avg_hold_time_bars | 9.0833 |
| exposure | 0.2081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
