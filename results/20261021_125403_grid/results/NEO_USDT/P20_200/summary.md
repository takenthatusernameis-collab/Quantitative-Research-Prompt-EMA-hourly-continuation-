# EMA Hourly Continuation — NEO/USDT P20_200

**Symbol:** NEO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7251 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.8941 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -1.5838 |
| sortino_ratio | -0.3808 |
| max_drawdown | 0.4072 |
| cagr | -0.1616 |
| net_avg_win | 69.3872 |
| net_avg_loss | -87.3398 |
| avg_hold_time_bars | 51.4070 |
| exposure | 0.6660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
