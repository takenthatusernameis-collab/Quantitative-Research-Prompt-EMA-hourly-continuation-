# EMA Hourly Continuation — ENJ/USDT P20_200

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6727 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9171 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -2.2782 |
| sortino_ratio | -0.6100 |
| max_drawdown | 0.5324 |
| cagr | -0.2531 |
| net_avg_win | 61.7185 |
| net_avg_loss | -84.4224 |
| avg_hold_time_bars | 39.6787 |
| exposure | 0.6511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
