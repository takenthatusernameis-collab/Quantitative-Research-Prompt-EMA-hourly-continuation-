# EMA Hourly Continuation — INJ/USDT P34_144

**Symbol:** INJ/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7265 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8649 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -1.8673 |
| sortino_ratio | -0.5119 |
| max_drawdown | 0.4657 |
| cagr | -0.2100 |
| net_avg_win | 68.1976 |
| net_avg_loss | -82.4924 |
| avg_hold_time_bars | 22.1962 |
| exposure | 0.3753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
