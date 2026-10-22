# EMA Hourly Continuation — ELON/USDT P8_89

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.7790 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -2.1872 |
| sortino_ratio | -0.7697 |
| max_drawdown | 0.6008 |
| cagr | -0.2983 |
| net_avg_win | 70.3753 |
| net_avg_loss | -85.1503 |
| avg_hold_time_bars | 19.9062 |
| exposure | 0.5501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
