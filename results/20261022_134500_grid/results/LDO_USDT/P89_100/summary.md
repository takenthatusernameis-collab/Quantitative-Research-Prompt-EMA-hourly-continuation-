# EMA Hourly Continuation — LDO/USDT P89_100

**Symbol:** LDO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.3003 |
| net_win_rate | 0.3780 |
| gross_profit_factor | 0.7238 |
| gross_win_rate | 0.4063 |
| sharpe_ratio | -9.5442 |
| sortino_ratio | -3.4462 |
| max_drawdown | 0.9899 |
| cagr | -0.8389 |
| net_avg_win | 17.7002 |
| net_avg_loss | -35.8125 |
| avg_hold_time_bars | 1.8913 |
| exposure | 0.0546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
