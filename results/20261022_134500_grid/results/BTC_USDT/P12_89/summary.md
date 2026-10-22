# EMA Hourly Continuation — BTC/USDT P12_89

**Symbol:** BTC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.4482 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9709 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -5.5716 |
| sortino_ratio | -1.9128 |
| max_drawdown | 0.9376 |
| cagr | -0.6195 |
| net_avg_win | 23.3329 |
| net_avg_loss | -46.7544 |
| avg_hold_time_bars | 20.1901 |
| exposure | 0.5564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
