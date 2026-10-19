# EMA Hourly Continuation — JTO/USDT P50_89

**Symbol:** JTO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.5090 |
| net_win_rate | 0.4482 |
| gross_profit_factor | 0.8394 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -5.2983 |
| sortino_ratio | -1.9050 |
| max_drawdown | 0.9054 |
| cagr | -0.6048 |
| net_avg_win | 31.8349 |
| net_avg_loss | -50.7945 |
| avg_hold_time_bars | 4.7713 |
| exposure | 0.1423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
