# EMA Hourly Continuation — EDU/USDT P144_200

**Symbol:** EDU/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.6232 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.8241 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -2.3152 |
| sortino_ratio | -0.4940 |
| max_drawdown | 0.4701 |
| cagr | -0.2035 |
| net_avg_win | 71.5380 |
| net_avg_loss | -92.7456 |
| avg_hold_time_bars | 6.9735 |
| exposure | 0.0713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
