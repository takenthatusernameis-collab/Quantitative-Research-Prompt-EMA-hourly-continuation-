# EMA Hourly Continuation — KCS/USDT P12_20

**Symbol:** KCS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1435 |
| net_profit_factor | 0.1084 |
| net_win_rate | 0.2307 |
| gross_profit_factor | 0.6234 |
| gross_win_rate | 0.3387 |
| sharpe_ratio | -22.7291 |
| sortino_ratio | -13.8703 |
| max_drawdown | 1.0000 |
| cagr | -0.9996 |
| net_avg_win | 3.6749 |
| net_avg_loss | -10.1598 |
| avg_hold_time_bars | 2.6885 |
| exposure | 0.1754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
