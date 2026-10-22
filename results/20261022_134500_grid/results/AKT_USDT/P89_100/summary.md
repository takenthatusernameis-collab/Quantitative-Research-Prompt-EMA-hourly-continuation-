# EMA Hourly Continuation — AKT/USDT P89_100

**Symbol:** AKT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.3061 |
| net_win_rate | 0.4066 |
| gross_profit_factor | 0.8505 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -8.6183 |
| sortino_ratio | -3.0171 |
| max_drawdown | 0.9835 |
| cagr | -0.8026 |
| net_avg_win | 17.6269 |
| net_avg_loss | -39.4603 |
| avg_hold_time_bars | 2.1074 |
| exposure | 0.0580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
