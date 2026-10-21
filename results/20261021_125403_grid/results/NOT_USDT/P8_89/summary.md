# EMA Hourly Continuation — NOT/USDT P8_89

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.9258 |
| net_win_rate | 0.5286 |
| gross_profit_factor | 1.1062 |
| gross_win_rate | 0.5286 |
| sharpe_ratio | -0.4077 |
| sortino_ratio | -0.1145 |
| max_drawdown | 0.2599 |
| cagr | -0.0561 |
| net_avg_win | 84.0869 |
| net_avg_loss | -101.8558 |
| avg_hold_time_bars | 40.0763 |
| exposure | 0.6909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
