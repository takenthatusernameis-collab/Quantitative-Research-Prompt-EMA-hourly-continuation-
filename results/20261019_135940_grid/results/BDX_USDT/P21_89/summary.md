# EMA Hourly Continuation — BDX/USDT P21_89

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1227 |
| net_profit_factor | 0.3244 |
| net_win_rate | 0.3089 |
| gross_profit_factor | 0.7474 |
| gross_win_rate | 0.3537 |
| sharpe_ratio | -16.8425 |
| sortino_ratio | -8.7120 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 12.6713 |
| net_avg_loss | -17.4556 |
| avg_hold_time_bars | 5.5485 |
| exposure | 0.3095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
