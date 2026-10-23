# EMA Hourly Continuation — DYDX/USDT P12_144

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7389 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0344 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -1.8785 |
| sortino_ratio | -0.5330 |
| max_drawdown | 0.4818 |
| cagr | -0.2217 |
| net_avg_win | 64.8144 |
| net_avg_loss | -90.8307 |
| avg_hold_time_bars | 40.1696 |
| exposure | 0.7322 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
