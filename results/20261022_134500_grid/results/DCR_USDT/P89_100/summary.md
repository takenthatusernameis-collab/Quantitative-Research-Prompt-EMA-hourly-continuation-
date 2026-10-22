# EMA Hourly Continuation — DCR/USDT P89_100

**Symbol:** DCR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.2337 |
| net_win_rate | 0.3619 |
| gross_profit_factor | 0.7228 |
| gross_win_rate | 0.4079 |
| sharpe_ratio | -9.9488 |
| sortino_ratio | -3.6336 |
| max_drawdown | 0.9910 |
| cagr | -0.8454 |
| net_avg_win | 13.2578 |
| net_avg_loss | -32.1708 |
| avg_hold_time_bars | 2.8492 |
| exposure | 0.0812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
