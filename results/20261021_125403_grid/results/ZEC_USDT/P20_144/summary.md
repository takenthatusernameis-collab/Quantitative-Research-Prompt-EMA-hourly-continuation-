# EMA Hourly Continuation — ZEC/USDT P20_144

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.9962 |
| net_win_rate | 0.5422 |
| gross_profit_factor | 1.1790 |
| gross_win_rate | 0.5422 |
| sharpe_ratio | 0.0380 |
| sortino_ratio | 0.0105 |
| max_drawdown | 0.1499 |
| cagr | -0.0027 |
| net_avg_win | 87.8189 |
| net_avg_loss | -104.4242 |
| avg_hold_time_bars | 31.2262 |
| exposure | 0.5209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
