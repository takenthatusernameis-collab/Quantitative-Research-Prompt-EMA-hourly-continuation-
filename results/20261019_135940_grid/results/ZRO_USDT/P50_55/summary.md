# EMA Hourly Continuation — ZRO/USDT P50_55

**Symbol:** ZRO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 770 |
| net_profit_factor | 0.3050 |
| net_win_rate | 0.3961 |
| gross_profit_factor | 0.7338 |
| gross_win_rate | 0.4130 |
| sharpe_ratio | -10.7420 |
| sortino_ratio | -4.4437 |
| max_drawdown | 0.9961 |
| cagr | -0.9074 |
| net_avg_win | 14.3323 |
| net_avg_loss | -30.8225 |
| avg_hold_time_bars | 1.6948 |
| exposure | 0.0639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
