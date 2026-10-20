# EMA Hourly Continuation — BABYDOGE/USDT P144_200

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 13 |
| net_profit_factor | 0.7746 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8532 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -0.2835 |
| sortino_ratio | -0.0144 |
| max_drawdown | 0.0525 |
| cagr | -0.0067 |
| net_avg_win | 96.1751 |
| net_avg_loss | -106.4212 |
| avg_hold_time_bars | 17.6154 |
| exposure | 0.0104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
