# EMA Hourly Continuation — ENS/USDT P20_21

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 148 |
| net_profit_factor | 0.8250 |
| net_win_rate | 0.5473 |
| gross_profit_factor | 1.2019 |
| gross_win_rate | 0.5473 |
| sharpe_ratio | -0.7231 |
| sortino_ratio | -0.1272 |
| max_drawdown | 0.1950 |
| cagr | -0.0572 |
| net_avg_win | 80.0526 |
| net_avg_loss | -117.3149 |
| avg_hold_time_bars | 5.3716 |
| exposure | 0.0361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
