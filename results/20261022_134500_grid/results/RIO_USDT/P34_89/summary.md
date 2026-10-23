# EMA Hourly Continuation — RIO/USDT P34_89

**Symbol:** RIO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 829 |
| net_profit_factor | 0.5266 |
| net_win_rate | 0.4041 |
| gross_profit_factor | 0.7504 |
| gross_win_rate | 0.4065 |
| sharpe_ratio | -6.8750 |
| sortino_ratio | -2.7841 |
| max_drawdown | 0.9675 |
| cagr | -0.7425 |
| net_avg_win | 32.0636 |
| net_avg_loss | -41.2929 |
| avg_hold_time_bars | 5.7877 |
| exposure | 0.2203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
