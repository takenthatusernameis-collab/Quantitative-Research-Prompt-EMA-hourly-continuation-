# EMA Hourly Continuation — P2P/USDT P50_200

**Symbol:** P2P/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6271 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.8047 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -2.8260 |
| sortino_ratio | -0.7493 |
| max_drawdown | 0.6266 |
| cagr | -0.3001 |
| net_avg_win | 63.8078 |
| net_avg_loss | -78.5744 |
| avg_hold_time_bars | 21.6676 |
| exposure | 0.3526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
