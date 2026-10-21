# EMA Hourly Continuation — WOO/USDT P100_144

**Symbol:** WOO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.6049 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8288 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -2.6191 |
| sortino_ratio | -0.6104 |
| max_drawdown | 0.5219 |
| cagr | -0.2453 |
| net_avg_win | 64.1248 |
| net_avg_loss | -87.8517 |
| avg_hold_time_bars | 5.5993 |
| exposure | 0.0680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
