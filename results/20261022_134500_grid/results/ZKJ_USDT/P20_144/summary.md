# EMA Hourly Continuation — ZKJ/USDT P20_144

**Symbol:** ZKJ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.2334 |
| net_win_rate | 0.3233 |
| gross_profit_factor | 0.5818 |
| gross_win_rate | 0.3947 |
| sharpe_ratio | -6.8206 |
| sortino_ratio | -1.6244 |
| max_drawdown | 0.8876 |
| cagr | -0.5753 |
| net_avg_win | 31.2745 |
| net_avg_loss | -64.0299 |
| avg_hold_time_bars | 69.5902 |
| exposure | 0.8414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
