# EMA Hourly Continuation — API3/USDT P26_50

**Symbol:** API3/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.5175 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.9516 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -7.7045 |
| sortino_ratio | -3.3959 |
| max_drawdown | 0.9843 |
| cagr | -0.8080 |
| net_avg_win | 24.8990 |
| net_avg_loss | -37.4975 |
| avg_hold_time_bars | 4.1281 |
| exposure | 0.1816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
