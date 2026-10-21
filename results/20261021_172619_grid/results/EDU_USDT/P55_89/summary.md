# EMA Hourly Continuation — EDU/USDT P55_89

**Symbol:** EDU/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.6003 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8200 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -3.0866 |
| sortino_ratio | -0.8721 |
| max_drawdown | 0.6443 |
| cagr | -0.3300 |
| net_avg_win | 53.3620 |
| net_avg_loss | -73.6596 |
| avg_hold_time_bars | 6.5899 |
| exposure | 0.1178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
