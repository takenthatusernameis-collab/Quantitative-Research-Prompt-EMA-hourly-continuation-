# EMA Hourly Continuation — DOGS/USDT P34_89

**Symbol:** DOGS/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.6112 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9027 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -4.3258 |
| sortino_ratio | -1.6574 |
| max_drawdown | 0.8150 |
| cagr | -0.5421 |
| net_avg_win | 42.6419 |
| net_avg_loss | -64.0060 |
| avg_hold_time_bars | 7.1946 |
| exposure | 0.2393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
