# EMA Hourly Continuation — NEO/USDT P26_55

**Symbol:** NEO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.3167 |
| net_win_rate | 0.4109 |
| gross_profit_factor | 0.6769 |
| gross_win_rate | 0.4260 |
| sharpe_ratio | -9.3127 |
| sortino_ratio | -4.0233 |
| max_drawdown | 0.9937 |
| cagr | -0.8661 |
| net_avg_win | 12.0266 |
| net_avg_loss | -26.4883 |
| avg_hold_time_bars | 4.6170 |
| exposure | 0.1956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
