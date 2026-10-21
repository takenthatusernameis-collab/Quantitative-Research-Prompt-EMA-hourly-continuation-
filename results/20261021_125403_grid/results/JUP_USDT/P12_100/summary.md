# EMA Hourly Continuation — JUP/USDT P12_100

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.8148 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9645 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -1.6121 |
| sortino_ratio | -0.5174 |
| max_drawdown | 0.5312 |
| cagr | -0.2133 |
| net_avg_win | 80.9585 |
| net_avg_loss | -93.6447 |
| avg_hold_time_bars | 22.3886 |
| exposure | 0.5160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
