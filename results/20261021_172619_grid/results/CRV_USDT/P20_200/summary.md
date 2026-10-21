# EMA Hourly Continuation — CRV/USDT P20_200

**Symbol:** CRV/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.8253 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9735 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.1133 |
| sortino_ratio | -0.2812 |
| max_drawdown | 0.3326 |
| cagr | -0.1228 |
| net_avg_win | 85.9966 |
| net_avg_loss | -100.9265 |
| avg_hold_time_bars | 41.7284 |
| exposure | 0.5937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
