# EMA Hourly Continuation — SOL/USDT P50_89

**Symbol:** SOL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.4290 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8772 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -6.6100 |
| sortino_ratio | -2.3681 |
| max_drawdown | 0.9515 |
| cagr | -0.6962 |
| net_avg_win | 24.6043 |
| net_avg_loss | -47.3890 |
| avg_hold_time_bars | 4.4228 |
| exposure | 0.1289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
