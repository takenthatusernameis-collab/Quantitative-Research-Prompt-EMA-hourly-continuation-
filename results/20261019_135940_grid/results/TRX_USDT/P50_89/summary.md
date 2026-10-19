# EMA Hourly Continuation — TRX/USDT P50_89

**Symbol:** TRX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.1993 |
| net_win_rate | 0.3243 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -11.2983 |
| sortino_ratio | -4.1550 |
| max_drawdown | 0.9964 |
| cagr | -0.8932 |
| net_avg_win | 12.9852 |
| net_avg_loss | -31.2660 |
| avg_hold_time_bars | 4.9610 |
| exposure | 0.1328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
