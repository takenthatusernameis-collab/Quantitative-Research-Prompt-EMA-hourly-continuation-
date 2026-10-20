# EMA Hourly Continuation — KSM/USDT P12_34

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1288 |
| net_profit_factor | 0.4410 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.8811 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -9.1718 |
| sortino_ratio | -4.6379 |
| max_drawdown | 0.9970 |
| cagr | -0.8996 |
| net_avg_win | 13.7730 |
| net_avg_loss | -24.8721 |
| avg_hold_time_bars | 4.3494 |
| exposure | 0.2546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
