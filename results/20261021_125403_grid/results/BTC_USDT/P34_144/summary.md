# EMA Hourly Continuation — BTC/USDT P34_144

**Symbol:** BTC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.6707 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0336 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -2.2277 |
| sortino_ratio | -0.5792 |
| max_drawdown | 0.5355 |
| cagr | -0.2334 |
| net_avg_win | 56.9933 |
| net_avg_loss | -87.7437 |
| avg_hold_time_bars | 25.0053 |
| exposure | 0.3741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
