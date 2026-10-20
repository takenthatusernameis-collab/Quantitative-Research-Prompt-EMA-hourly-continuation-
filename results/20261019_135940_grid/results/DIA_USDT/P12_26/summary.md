# EMA Hourly Continuation — DIA/USDT P12_26

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1332 |
| net_profit_factor | 0.3482 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.7796 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -9.3663 |
| sortino_ratio | -4.8187 |
| max_drawdown | 0.9975 |
| cagr | -0.9064 |
| net_avg_win | 9.0331 |
| net_avg_loss | -20.6255 |
| avg_hold_time_bars | 3.4392 |
| exposure | 0.2073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
