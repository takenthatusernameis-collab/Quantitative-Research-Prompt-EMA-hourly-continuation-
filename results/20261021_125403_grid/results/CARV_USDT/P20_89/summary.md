# EMA Hourly Continuation — CARV/USDT P20_89

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7651 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -2.0077 |
| sortino_ratio | -0.6388 |
| max_drawdown | 0.5107 |
| cagr | -0.2549 |
| net_avg_win | 75.0862 |
| net_avg_loss | -92.8933 |
| avg_hold_time_bars | 16.9177 |
| exposure | 0.3818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
