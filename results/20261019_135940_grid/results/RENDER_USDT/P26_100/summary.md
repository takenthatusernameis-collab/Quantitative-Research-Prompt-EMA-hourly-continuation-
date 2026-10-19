# EMA Hourly Continuation — RENDER/USDT P26_100

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.6866 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 1.0173 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -3.1126 |
| sortino_ratio | -1.1186 |
| max_drawdown | 0.7064 |
| cagr | -0.4148 |
| net_avg_win | 53.2988 |
| net_avg_loss | -78.1852 |
| avg_hold_time_bars | 11.0925 |
| exposure | 0.3290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
