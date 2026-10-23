# EMA Hourly Continuation — KSM/USDT P26_144

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6446 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9740 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -3.0954 |
| sortino_ratio | -0.8591 |
| max_drawdown | 0.6831 |
| cagr | -0.3468 |
| net_avg_win | 63.0377 |
| net_avg_loss | -87.1783 |
| avg_hold_time_bars | 28.9302 |
| exposure | 0.5273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
