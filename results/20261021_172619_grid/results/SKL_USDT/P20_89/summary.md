# EMA Hourly Continuation — SKL/USDT P20_89

**Symbol:** SKL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.8055 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9982 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5343 |
| sortino_ratio | -0.4845 |
| max_drawdown | 0.4819 |
| cagr | -0.2006 |
| net_avg_win | 73.3036 |
| net_avg_loss | -91.0035 |
| avg_hold_time_bars | 17.7202 |
| exposure | 0.3915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
