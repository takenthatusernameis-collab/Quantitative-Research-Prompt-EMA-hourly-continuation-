# EMA Hourly Continuation — CAKE/USDT P12_200

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.8870 |
| net_win_rate | 0.5265 |
| gross_profit_factor | 1.0992 |
| gross_win_rate | 0.5265 |
| sharpe_ratio | -0.6705 |
| sortino_ratio | -0.1725 |
| max_drawdown | 0.3225 |
| cagr | -0.0793 |
| net_avg_win | 87.0422 |
| net_avg_loss | -109.1023 |
| avg_hold_time_bars | 47.6324 |
| exposure | 0.6950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
