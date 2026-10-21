# EMA Hourly Continuation — KAS/USDT P55_144

**Symbol:** KAS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.6723 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.8619 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -2.0420 |
| sortino_ratio | -0.5307 |
| max_drawdown | 0.4668 |
| cagr | -0.2156 |
| net_avg_win | 59.2875 |
| net_avg_loss | -79.6203 |
| avg_hold_time_bars | 13.6697 |
| exposure | 0.2069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
