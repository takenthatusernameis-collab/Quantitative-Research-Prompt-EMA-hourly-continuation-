# EMA Hourly Continuation — CRO/USDT P8_50

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1196 |
| net_profit_factor | 0.4019 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.8413 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -9.1299 |
| sortino_ratio | -4.4361 |
| max_drawdown | 0.9964 |
| cagr | -0.8920 |
| net_avg_win | 12.8748 |
| net_avg_loss | -24.6413 |
| avg_hold_time_bars | 8.0234 |
| exposure | 0.4362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
