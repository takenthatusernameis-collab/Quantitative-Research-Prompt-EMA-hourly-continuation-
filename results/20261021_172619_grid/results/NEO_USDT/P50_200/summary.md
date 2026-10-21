# EMA Hourly Continuation — NEO/USDT P50_200

**Symbol:** NEO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.7303 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9247 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -1.6363 |
| sortino_ratio | -0.4122 |
| max_drawdown | 0.4121 |
| cagr | -0.1728 |
| net_avg_win | 67.5408 |
| net_avg_loss | -87.8567 |
| avg_hold_time_bars | 27.2724 |
| exposure | 0.3868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
