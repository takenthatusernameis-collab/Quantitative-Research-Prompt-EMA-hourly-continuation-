# EMA Hourly Continuation — KAS/USDT P89_100

**Symbol:** KAS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.2232 |
| net_win_rate | 0.3764 |
| gross_profit_factor | 0.6831 |
| gross_win_rate | 0.4099 |
| sharpe_ratio | -10.1164 |
| sortino_ratio | -3.6904 |
| max_drawdown | 0.9929 |
| cagr | -0.8609 |
| net_avg_win | 12.0911 |
| net_avg_loss | -32.6930 |
| avg_hold_time_bars | 1.9856 |
| exposure | 0.0566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
