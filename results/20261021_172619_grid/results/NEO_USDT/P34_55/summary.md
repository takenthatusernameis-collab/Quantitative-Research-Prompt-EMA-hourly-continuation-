# EMA Hourly Continuation — NEO/USDT P34_55

**Symbol:** NEO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5902 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.8952 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.9274 |
| sortino_ratio | -0.7903 |
| max_drawdown | 0.5956 |
| cagr | -0.3016 |
| net_avg_win | 50.6198 |
| net_avg_loss | -78.7756 |
| avg_hold_time_bars | 6.1728 |
| exposure | 0.0990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
