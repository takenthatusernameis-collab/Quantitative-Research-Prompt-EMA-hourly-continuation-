# EMA Hourly Continuation — BLZ/USDT P12_34

**Symbol:** BLZ/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1270 |
| net_profit_factor | 0.4569 |
| net_win_rate | 0.3961 |
| gross_profit_factor | 0.8475 |
| gross_win_rate | 0.4181 |
| sharpe_ratio | -10.4843 |
| sortino_ratio | -5.2662 |
| max_drawdown | 0.9986 |
| cagr | -0.9252 |
| net_avg_win | 16.7024 |
| net_avg_loss | -23.9724 |
| avg_hold_time_bars | 5.1220 |
| exposure | 0.2944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
