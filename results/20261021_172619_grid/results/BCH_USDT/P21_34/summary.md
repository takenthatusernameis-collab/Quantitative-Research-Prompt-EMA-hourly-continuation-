# EMA Hourly Continuation — BCH/USDT P21_34

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.5540 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8305 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -2.9169 |
| sortino_ratio | -0.6819 |
| max_drawdown | 0.5485 |
| cagr | -0.2687 |
| net_avg_win | 55.4187 |
| net_avg_loss | -84.7532 |
| avg_hold_time_bars | 5.5865 |
| exposure | 0.0675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
