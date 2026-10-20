# EMA Hourly Continuation — ZEN/USDT P21_34

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1213 |
| net_profit_factor | 0.3280 |
| net_win_rate | 0.4213 |
| gross_profit_factor | 0.7883 |
| gross_win_rate | 0.4452 |
| sharpe_ratio | -10.6045 |
| sortino_ratio | -5.2378 |
| max_drawdown | 0.9987 |
| cagr | -0.9298 |
| net_avg_win | 9.5389 |
| net_avg_loss | -21.1705 |
| avg_hold_time_bars | 2.3735 |
| exposure | 0.1309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
