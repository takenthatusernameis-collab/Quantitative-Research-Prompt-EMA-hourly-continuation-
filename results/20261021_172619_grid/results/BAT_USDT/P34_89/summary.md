# EMA Hourly Continuation — BAT/USDT P34_89

**Symbol:** BAT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6499 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9003 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.8796 |
| sortino_ratio | -0.9198 |
| max_drawdown | 0.6714 |
| cagr | -0.3433 |
| net_avg_win | 50.8669 |
| net_avg_loss | -71.0983 |
| avg_hold_time_bars | 10.2180 |
| exposure | 0.2322 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
