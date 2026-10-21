# EMA Hourly Continuation — WIN/USDT P50_200

**Symbol:** WIN/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.6968 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9051 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -1.7423 |
| sortino_ratio | -0.3985 |
| max_drawdown | 0.4281 |
| cagr | -0.1684 |
| net_avg_win | 69.2593 |
| net_avg_loss | -91.2392 |
| avg_hold_time_bars | 33.4319 |
| exposure | 0.3905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
