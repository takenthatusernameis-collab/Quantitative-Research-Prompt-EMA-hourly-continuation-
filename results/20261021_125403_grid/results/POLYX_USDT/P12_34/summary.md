# EMA Hourly Continuation — POLYX/USDT P12_34

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.7016 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9932 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -3.3807 |
| sortino_ratio | -1.2987 |
| max_drawdown | 0.7894 |
| cagr | -0.4473 |
| net_avg_win | 51.4423 |
| net_avg_loss | -71.3039 |
| avg_hold_time_bars | 6.6950 |
| exposure | 0.2185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
