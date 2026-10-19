# EMA Hourly Continuation — TIA/USDT P55_200

**Symbol:** TIA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7710 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0245 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.5927 |
| sortino_ratio | -0.4165 |
| max_drawdown | 0.4103 |
| cagr | -0.1796 |
| net_avg_win | 76.6835 |
| net_avg_loss | -100.0415 |
| avg_hold_time_bars | 23.9125 |
| exposure | 0.3728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
