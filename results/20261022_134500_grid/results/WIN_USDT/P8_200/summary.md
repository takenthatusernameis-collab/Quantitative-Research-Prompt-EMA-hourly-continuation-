# EMA Hourly Continuation — WIN/USDT P8_200

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6196 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0238 |
| gross_win_rate | 0.5253 |
| sharpe_ratio | -2.3336 |
| sortino_ratio | -0.6249 |
| max_drawdown | 0.6407 |
| cagr | -0.2700 |
| net_avg_win | 46.8318 |
| net_avg_loss | -77.6318 |
| avg_hold_time_bars | 46.7120 |
| exposure | 0.7962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
