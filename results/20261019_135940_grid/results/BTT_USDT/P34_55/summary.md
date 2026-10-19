# EMA Hourly Continuation — BTT/USDT P34_55

**Symbol:** BTT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.2054 |
| net_win_rate | 0.3008 |
| gross_profit_factor | 0.6789 |
| gross_win_rate | 0.3840 |
| sharpe_ratio | -14.9268 |
| sortino_ratio | -6.8003 |
| max_drawdown | 0.9999 |
| cagr | -0.9750 |
| net_avg_win | 9.5399 |
| net_avg_loss | -19.9752 |
| avg_hold_time_bars | 3.6648 |
| exposure | 0.1501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
