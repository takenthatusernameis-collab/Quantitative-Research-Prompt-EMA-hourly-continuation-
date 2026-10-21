# EMA Hourly Continuation — FLOKI/USDT P55_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8354 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0270 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -1.0019 |
| sortino_ratio | -0.2676 |
| max_drawdown | 0.2859 |
| cagr | -0.1171 |
| net_avg_win | 77.4494 |
| net_avg_loss | -95.9788 |
| avg_hold_time_bars | 17.8439 |
| exposure | 0.2806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
