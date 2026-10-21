# EMA Hourly Continuation — API3/USDT P55_200

**Symbol:** API3/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7612 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9366 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -1.5568 |
| sortino_ratio | -0.3961 |
| max_drawdown | 0.3942 |
| cagr | -0.1672 |
| net_avg_win | 76.2181 |
| net_avg_loss | -93.4595 |
| avg_hold_time_bars | 26.7492 |
| exposure | 0.3879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
