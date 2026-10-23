# EMA Hourly Continuation — QI/USDT P20_21

**Symbol:** QI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1087 |
| net_profit_factor | 0.1389 |
| net_win_rate | 0.3073 |
| gross_profit_factor | 0.5713 |
| gross_win_rate | 0.3901 |
| sharpe_ratio | -15.8258 |
| sortino_ratio | -7.7405 |
| max_drawdown | 1.0000 |
| cagr | -0.9862 |
| net_avg_win | 4.8308 |
| net_avg_loss | -15.4227 |
| avg_hold_time_bars | 2.5198 |
| exposure | 0.1239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
