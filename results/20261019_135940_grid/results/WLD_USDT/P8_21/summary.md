# EMA Hourly Continuation — WLD/USDT P8_21

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1692 |
| net_profit_factor | 0.4385 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8205 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -9.5409 |
| sortino_ratio | -5.5077 |
| max_drawdown | 0.9990 |
| cagr | -0.9359 |
| net_avg_win | 9.9628 |
| net_avg_loss | -19.5719 |
| avg_hold_time_bars | 2.7335 |
| exposure | 0.2102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
