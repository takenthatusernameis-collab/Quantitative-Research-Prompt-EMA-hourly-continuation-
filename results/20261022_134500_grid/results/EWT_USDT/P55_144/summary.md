# EMA Hourly Continuation — EWT/USDT P55_144

**Symbol:** EWT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.4252 |
| net_win_rate | 0.4016 |
| gross_profit_factor | 0.6536 |
| gross_win_rate | 0.4096 |
| sharpe_ratio | -5.5670 |
| sortino_ratio | -1.7444 |
| max_drawdown | 0.8895 |
| cagr | -0.5737 |
| net_avg_win | 32.6353 |
| net_avg_loss | -51.5165 |
| avg_hold_time_bars | 9.3012 |
| exposure | 0.2105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
