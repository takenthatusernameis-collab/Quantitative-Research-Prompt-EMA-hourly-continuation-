# EMA Hourly Continuation — JST/USDT P21_144

**Symbol:** JST/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.4619 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9591 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -4.2400 |
| sortino_ratio | -1.2223 |
| max_drawdown | 0.8063 |
| cagr | -0.4672 |
| net_avg_win | 33.3201 |
| net_avg_loss | -63.4680 |
| avg_hold_time_bars | 26.9201 |
| exposure | 0.5336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
