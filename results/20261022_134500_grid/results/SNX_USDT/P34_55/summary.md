# EMA Hourly Continuation — SNX/USDT P34_55

**Symbol:** SNX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 879 |
| net_profit_factor | 0.4860 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9917 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -7.2734 |
| sortino_ratio | -3.0303 |
| max_drawdown | 0.9788 |
| cagr | -0.7795 |
| net_avg_win | 22.8348 |
| net_avg_loss | -40.1424 |
| avg_hold_time_bars | 3.3106 |
| exposure | 0.1317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
