# EMA Hourly Continuation — ENS/USDT P21_34

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7287 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0449 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.8203 |
| sortino_ratio | -0.4559 |
| max_drawdown | 0.4473 |
| cagr | -0.1895 |
| net_avg_win | 71.0638 |
| net_avg_loss | -101.4438 |
| avg_hold_time_bars | 5.5066 |
| exposure | 0.0761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
