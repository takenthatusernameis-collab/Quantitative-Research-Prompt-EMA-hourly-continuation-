# EMA Hourly Continuation — EWT/USDT P26_100

**Symbol:** EWT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.4543 |
| net_win_rate | 0.4186 |
| gross_profit_factor | 0.7052 |
| gross_win_rate | 0.4290 |
| sharpe_ratio | -5.9275 |
| sortino_ratio | -2.1508 |
| max_drawdown | 0.9365 |
| cagr | -0.6541 |
| net_avg_win | 27.3735 |
| net_avg_loss | -43.3872 |
| avg_hold_time_bars | 9.4009 |
| exposure | 0.2889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
