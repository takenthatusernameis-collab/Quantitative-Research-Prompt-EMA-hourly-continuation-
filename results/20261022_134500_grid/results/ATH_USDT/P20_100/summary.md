# EMA Hourly Continuation — ATH/USDT P20_100

**Symbol:** ATH/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.7174 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0469 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -2.7916 |
| sortino_ratio | -1.0336 |
| max_drawdown | 0.6948 |
| cagr | -0.3848 |
| net_avg_win | 53.7358 |
| net_avg_loss | -76.3209 |
| avg_hold_time_bars | 13.4781 |
| exposure | 0.4168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
