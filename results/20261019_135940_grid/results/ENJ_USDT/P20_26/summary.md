# EMA Hourly Continuation — ENJ/USDT P20_26

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1206 |
| net_profit_factor | 0.2450 |
| net_win_rate | 0.3748 |
| gross_profit_factor | 0.7219 |
| gross_win_rate | 0.4245 |
| sharpe_ratio | -13.6864 |
| sortino_ratio | -6.8998 |
| max_drawdown | 0.9999 |
| cagr | -0.9721 |
| net_avg_win | 7.1767 |
| net_avg_loss | -17.5632 |
| avg_hold_time_bars | 1.9030 |
| exposure | 0.1039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
