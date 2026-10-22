# EMA Hourly Continuation — DCR/USDT P34_89

**Symbol:** DCR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.4752 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.8061 |
| gross_win_rate | 0.4383 |
| sharpe_ratio | -6.3935 |
| sortino_ratio | -2.4211 |
| max_drawdown | 0.9473 |
| cagr | -0.6857 |
| net_avg_win | 28.0858 |
| net_avg_loss | -43.3337 |
| avg_hold_time_bars | 7.4785 |
| exposure | 0.2440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
